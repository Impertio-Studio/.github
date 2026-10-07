#!/usr/bin/env python3
"""Detect the release version of an Impertio-Studio repository and extract its
CHANGELOG notes.

One manifest defines a repo's release version. This script finds that manifest,
reads the version, derives the `v<version>` tag, and pulls the matching section
out of `CHANGELOG.md` (Keep a Changelog format). It writes machine-readable
outputs to `$GITHUB_OUTPUT` when run inside GitHub Actions, and always prints a
human summary to stderr.

It fails loud (non-zero exit, clear message) when no manifest is found or a
manifest carries no resolvable version. It does NOT invent a version and does
NOT fall back to a different manifest to paper over a missing field: precedence
picks exactly one manifest per repo, and a broken manifest is an error, not a
silent skip.

Manifest precedence (most specific first):
  1. .claude-plugin/plugin.json  (Claude Code plugins)
  2. pyproject.toml              (Frappe / Python apps)
  3. package.json               (skill-packages / templates / JS apps)
  4. VERSION                     (language-agnostic plain-text fallback:
                                  docs / scaffolds / templates without any
                                  language manifest; one semver line)
  5. .claude-plugin/marketplace.json  with exactly one local plugin: the
                                  plugin.json at <source>/.claude-plugin/ (a
                                  plugin that keeps its runtime in a subfolder)

Notes are NOT required to be present here: on a genuine bump the caller workflow
enforces that a CHANGELOG section exists (notes_found=true). Keeping that policy
in the workflow keeps this script a pure reader.
"""

from __future__ import annotations

import json
import os
import re
import sys
import tomllib
from pathlib import Path


def die(msg: str) -> "NoReturn":  # type: ignore[name-defined]
    print(f"::error::detect-release: {msg}", file=sys.stderr)
    sys.exit(1)


def read_json_version(path: Path) -> str:
    data = json.loads(path.read_text(encoding="utf-8"))
    version = data.get("version")
    if not isinstance(version, str) or not version.strip():
        die(f"{path} has no string 'version' field")
    return version.strip()


# A plain-text VERSION file must hold exactly one semver line. This is stricter
# than the JSON/TOML readers on purpose: a schemaless text file has no field to
# key on, so the semver shape is the only guard against a stray "VERSION" file
# (e.g. licensing text) being mistaken for a release manifest. Fail loud, no
# guessing.
_SEMVER_RE = re.compile(r"^\d+\.\d+\.\d+(?:[-+][0-9A-Za-z.-]+)?$")


def read_version_file(path: Path) -> str:
    lines = [ln.strip() for ln in path.read_text(encoding="utf-8").splitlines()]
    nonblank = [ln for ln in lines if ln]
    if not nonblank:
        die(f"{path} is empty; expected a single semver line (e.g. 0.1.0)")
    if len(nonblank) > 1:
        die(f"{path} has multiple non-blank lines; expected a single semver line")
    version = nonblank[0]
    if not _SEMVER_RE.match(version):
        die(f"{path} content '{version}' is not a valid semver (e.g. 0.1.0)")
    return version


def read_module_version(module_file: Path) -> str | None:
    if not module_file.is_file():
        return None
    text = module_file.read_text(encoding="utf-8")
    m = re.search(r"""^__version__\s*=\s*['"]([^'"]+)['"]""", text, re.MULTILINE)
    return m.group(1).strip() if m else None


def read_pyproject_version(repo: Path, path: Path) -> str:
    data = tomllib.loads(path.read_text(encoding="utf-8"))
    project = data.get("project", {})

    # Static version wins.
    static = project.get("version")
    if isinstance(static, str) and static.strip():
        return static.strip()

    # Dynamic version (flit / hatch): resolve __version__ from the module.
    if "version" not in project.get("dynamic", []):
        die(f"{path} [project] has neither a static 'version' nor a dynamic one")

    # hatch: explicit path to the file holding __version__.
    hatch_path = (
        data.get("tool", {}).get("hatch", {}).get("version", {}).get("path")
    )
    if isinstance(hatch_path, str):
        v = read_module_version(repo / hatch_path)
        if v:
            return v
        die(f"[tool.hatch.version].path '{hatch_path}' holds no __version__")

    # flit: module name is explicit or derived from the project name.
    flit_module = (
        data.get("tool", {}).get("flit", {}).get("module", {}).get("name")
    )
    name = project.get("name")
    module = flit_module or (name.replace("-", "_") if isinstance(name, str) else None)
    if not module:
        die(f"{path} declares a dynamic version but no resolvable module name")

    for candidate in (repo / module / "__init__.py", repo / f"{module}.py"):
        v = read_module_version(candidate)
        if v:
            return v
    die(
        f"{path} declares a dynamic version but no __version__ found in "
        f"'{module}/__init__.py' or '{module}.py'"
    )


def detect(repo: Path) -> tuple[str, str]:
    """Return (manifest_type, version) using strict precedence."""
    plugin = repo / ".claude-plugin" / "plugin.json"
    if plugin.is_file():
        return "plugin.json", read_json_version(plugin)

    pyproject = repo / "pyproject.toml"
    if pyproject.is_file():
        return "pyproject.toml", read_pyproject_version(repo, pyproject)

    package = repo / "package.json"
    if package.is_file():
        return "package.json", read_json_version(package)

    version_file = repo / "VERSION"
    if version_file.is_file():
        return "VERSION", read_version_file(version_file)

    marketplace = repo / ".claude-plugin" / "marketplace.json"
    if marketplace.is_file():
        found = read_marketplace_plugin(repo, marketplace)
        if found is not None:
            return found

    die(
        f"no release manifest found in '{repo}'. Expected one of: "
        ".claude-plugin/plugin.json, pyproject.toml, package.json, VERSION, "
        "or a .claude-plugin/marketplace.json whose one local plugin has a "
        ".claude-plugin/plugin.json inside the repo"
    )


def read_marketplace_plugin(repo: Path, marketplace: Path) -> tuple[str, str] | None:
    """The plugin.json of the one local plugin a marketplace.json lists, if there is one.

    A Claude Code plugin repo may keep its runtime in a subfolder: the root then holds only
    .claude-plugin/marketplace.json, whose plugin entry has a local `source` such as "./plugin",
    and the manifest lives at <source>/.claude-plugin/plugin.json (tmux-orchestration since
    October 2026). This is the last place looked at, so a repo with any other manifest keeps it.
    A remote source, a source outside the repo or a source without a plugin.json is no manifest;
    two or more local plugins make the version ambiguous and fail loud.
    """
    try:
        data = json.loads(marketplace.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        die(f"{marketplace} is not valid JSON: {exc}")
    plugins = data.get("plugins") if isinstance(data, dict) else None
    root = repo.resolve()
    found: list[Path] = []
    for entry in plugins if isinstance(plugins, list) else []:
        source = entry.get("source") if isinstance(entry, dict) else None
        if not isinstance(source, str) or "://" in source:
            continue
        manifest = (repo / source / ".claude-plugin" / "plugin.json").resolve()
        if manifest.is_file() and manifest.is_relative_to(root):
            found.append(manifest)
    if len(found) > 1:
        die(
            f"{marketplace} lists {len(found)} local plugins with a plugin.json; "
            "the release version of the repo is ambiguous"
        )
    if not found:
        return None
    rel = found[0].relative_to(root).as_posix()
    return f"marketplace.json -> {rel}", read_json_version(found[0])


def extract_notes(repo: Path, version: str) -> str | None:
    """Return the CHANGELOG body for `version`, or None if absent."""
    changelog = repo / "CHANGELOG.md"
    if not changelog.is_file():
        return None
    lines = changelog.read_text(encoding="utf-8").splitlines()
    # Heading like: ## [0.8.1] - 2026-07-06   (date optional)
    head_re = re.compile(r"^##\s*\[" + re.escape(version) + r"\](?:\s|$)")
    start = None
    for i, line in enumerate(lines):
        if head_re.match(line):
            start = i + 1
            break
    if start is None:
        return None
    body: list[str] = []
    for line in lines[start:]:
        if line.startswith("## "):
            break
        body.append(line)
    text = "\n".join(body).strip("\n").strip()
    return text or None


def emit_output(name: str, value: str) -> None:
    out = os.environ.get("GITHUB_OUTPUT")
    if not out:
        return
    with open(out, "a", encoding="utf-8") as fh:
        if "\n" in value:
            delim = "EOF_DETECT_RELEASE"
            fh.write(f"{name}<<{delim}\n{value}\n{delim}\n")
        else:
            fh.write(f"{name}={value}\n")


def main() -> None:
    repo = Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    if not repo.is_dir():
        die(f"repo path '{repo}' is not a directory")

    manifest_type, version = detect(repo)
    tag = f"v{version}"
    notes = extract_notes(repo, version)

    emit_output("version", version)
    emit_output("tag", tag)
    emit_output("manifest", manifest_type)
    emit_output("notes_found", "true" if notes is not None else "false")

    notes_file = os.environ.get("RELEASE_NOTES_FILE")
    if notes_file and notes is not None:
        Path(notes_file).write_text(notes + "\n", encoding="utf-8")

    print(
        f"detect-release: manifest={manifest_type} version={version} tag={tag} "
        f"notes_found={'true' if notes is not None else 'false'}",
        file=sys.stderr,
    )


if __name__ == "__main__":
    main()
