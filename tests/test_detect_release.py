"""Tests for scripts/detect-release.py.

Run: python3 tests/test_detect_release.py -v
"""

from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

sys.dont_write_bytecode = True  # importing the script must leave no __pycache__ in scripts/
SCRIPT = Path(__file__).resolve().parent.parent / "scripts" / "detect-release.py"
spec = importlib.util.spec_from_file_location("detect_release", SCRIPT)
detect_release = importlib.util.module_from_spec(spec)
spec.loader.exec_module(detect_release)


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")


def plugin_json(version: str) -> str:
    return json.dumps({"name": "demo", "version": version})


def marketplace(*sources) -> str:
    return json.dumps(
        {"name": "demo", "plugins": [{"name": f"p{i}", "source": s} for i, s in enumerate(sources)]}
    )


def run_script(repo: Path) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(SCRIPT), str(repo)], capture_output=True, text=True
    )


class DetectRelease(unittest.TestCase):
    def setUp(self) -> None:
        self.tmp = tempfile.TemporaryDirectory()
        self.repo = Path(self.tmp.name)

    def tearDown(self) -> None:
        self.tmp.cleanup()

    def test_root_plugin_json(self) -> None:
        write(self.repo / ".claude-plugin" / "plugin.json", plugin_json("1.2.3"))
        self.assertEqual(detect_release.detect(self.repo), ("plugin.json", "1.2.3"))

    def test_marketplace_with_one_local_plugin(self) -> None:
        # The layout of tmux-orchestration since its runtime moved to plugin/.
        write(self.repo / ".claude-plugin" / "marketplace.json", marketplace("./plugin"))
        write(self.repo / "plugin" / ".claude-plugin" / "plugin.json", plugin_json("0.42.0"))
        self.assertEqual(
            detect_release.detect(self.repo),
            ("marketplace.json -> plugin/.claude-plugin/plugin.json", "0.42.0"),
        )

    def test_root_plugin_json_wins_over_marketplace(self) -> None:
        write(self.repo / ".claude-plugin" / "plugin.json", plugin_json("2.0.0"))
        write(self.repo / ".claude-plugin" / "marketplace.json", marketplace("./plugin"))
        write(self.repo / "plugin" / ".claude-plugin" / "plugin.json", plugin_json("9.9.9"))
        self.assertEqual(detect_release.detect(self.repo), ("plugin.json", "2.0.0"))

    def test_package_json_wins_over_marketplace(self) -> None:
        # Strictly additive: a repo that has a manifest today keeps its version source.
        write(self.repo / "package.json", json.dumps({"version": "3.1.0"}))
        write(self.repo / ".claude-plugin" / "marketplace.json", marketplace("./plugin"))
        write(self.repo / "plugin" / ".claude-plugin" / "plugin.json", plugin_json("9.9.9"))
        self.assertEqual(detect_release.detect(self.repo), ("package.json", "3.1.0"))

    def test_marketplace_with_two_local_plugins_fails_loud(self) -> None:
        write(self.repo / ".claude-plugin" / "marketplace.json", marketplace("./a", "./b"))
        write(self.repo / "a" / ".claude-plugin" / "plugin.json", plugin_json("1.0.0"))
        write(self.repo / "b" / ".claude-plugin" / "plugin.json", plugin_json("2.0.0"))
        result = run_script(self.repo)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("2 local plugins", result.stderr)

    def test_marketplace_with_remote_source_only_fails_loud(self) -> None:
        write(
            self.repo / ".claude-plugin" / "marketplace.json",
            marketplace({"source": "github", "repo": "owner/name"}),
        )
        result = run_script(self.repo)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("no release manifest found", result.stderr)

    def test_marketplace_pointing_at_missing_plugin_json_fails_loud(self) -> None:
        write(self.repo / ".claude-plugin" / "marketplace.json", marketplace("./plugin"))
        result = run_script(self.repo)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("no release manifest found", result.stderr)

    def test_marketplace_source_outside_the_repo_is_ignored(self) -> None:
        # A sibling folder of the repo holds a plugin.json; a source that climbs out of the repo
        # must not become the version of this repo.
        outside = tempfile.TemporaryDirectory(dir=self.repo.parent)
        self.addCleanup(outside.cleanup)
        write(Path(outside.name) / ".claude-plugin" / "plugin.json", plugin_json("6.6.6"))
        write(
            self.repo / ".claude-plugin" / "marketplace.json",
            marketplace("../" + Path(outside.name).name),
        )
        result = run_script(self.repo)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("no release manifest found", result.stderr)

    def test_broken_marketplace_json_fails_loud(self) -> None:
        write(self.repo / ".claude-plugin" / "marketplace.json", "{not json")
        result = run_script(self.repo)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("marketplace.json", result.stderr)


if __name__ == "__main__":
    unittest.main()
