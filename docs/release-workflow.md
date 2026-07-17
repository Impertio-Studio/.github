# Org-brede release-workflow

Een herbruikbare GitHub Actions-workflow die voor elke Impertio-Studio repo de
release-stap automatiseert: op elke merge naar `main` maakt hij de git-tag
`v<version>` en publiceert hij een GitHub Release met de notes uit de CHANGELOG,
maar alleen wanneer de version daadwerkelijk is gebumpt.

De workflow is puur additief. Hij vervangt niets aan de bestaande commit-,
branch- en PR-afspraken uit `GIT_PRACTICES.md` (merge-commits, geen squash,
branches blijven staan, UPPERCASE-commits, 2 reviewers voor `main`). Hij neemt
alleen de laatste twee handmatige stappen van het release-proces over: het
zetten van de tag en het publiceren van de release.

## Het mechanisme

De workflow verzoent twee doelen die op het eerste gezicht botsen:

> "elke main-merge triggert een release" + "geen kapotte dubbele releases"

Dat lukt door de **version-bump** het echte release-signaal te maken, niet de
merge zelf:

1. Lees de version uit het manifest van de repo (zie precedentie hieronder).
2. Bestaat de tag `v<version>` al? Dan heeft deze merge de version niet gebumpt
   (bijvoorbeeld een docs-only merge). De workflow stopt schoon als no-op.
3. Bestaat de tag nog niet? Dan is de version gebumpt. De workflow maakt de tag
   `v<version>` op de merge-commit en publiceert een GitHub Release met de
   CHANGELOG-sectie voor die version als notes.

De operatie is idempotent: opnieuw draaien op dezelfde commit verandert niets.

## Version-manifest, precedentie

Elke repo heeft precies een manifest dat de release-version bepaalt. De workflow
detecteert het in deze volgorde (meest specifiek eerst):

1. `.claude-plugin/plugin.json` — Claude Code plugins
2. `pyproject.toml` — Frappe- en Python-apps (statische `[project].version` of
   een dynamische version via flit/hatch, uit `<module>/__init__.py`)
3. `package.json` — skill-packages, templates, JS-apps
4. `VERSION` — taal-agnostische fallback: een plain-text bestand op de repo-root
   met precies een semver-regel (bijvoorbeeld `0.1.0`). Bedoeld voor repos zonder
   taal-manifest, zoals docs-, template- en scaffold-repos, zodat ook die een
   conventionele version-plek hebben. Laagste precedentie: hij wordt alleen
   gelezen als geen van de drie manifesten hierboven bestaat.

Ontbreekt een manifest, of is de version niet leesbaar, dan faalt de workflow
luid. Er is geen stille fallback naar een ander manifest. Let op: dit geldt ook
voor `VERSION`. Bestaat er wel een `package.json` maar zonder `version`-veld, dan
faalt de workflow luid op die `package.json`; hij valt niet stilletjes terug op
een `VERSION`-bestand. Elk repo heeft precies een version-bron.

## Adoptie in een repo

1. Kopieer `docs/release.yml.template` uit deze repo naar
   `.github/workflows/release.yml` in je eigen repo.
2. Commit dat via de normale branch- en PR-flow (`GIT_PRACTICES.md`).
3. Zorg dat de repo een version-bron heeft op de voor z'n type conventionele
   plek: een taal-manifest (`.claude-plugin/plugin.json`, `pyproject.toml` of
   `package.json`), of, voor een repo zonder taal-manifest, een `VERSION`-bestand
   op de repo-root met een enkele semver-regel (bijvoorbeeld `0.1.0`).
4. Zorg dat de repo een `CHANGELOG.md` in Keep a Changelog-formaat heeft, met
   per version een `## [<version>]`-sectie. Een bump zonder bijbehorende
   CHANGELOG-sectie laat de workflow luid falen.

Vanaf dat moment: bij elke release (bump van de version + CHANGELOG-sectie, dan
merge naar `main`) zet de workflow automatisch de tag en de GitHub Release.

## Rechten

De workflow heeft `contents: write` nodig om tags en releases te maken. Zowel de
herbruikbare workflow als de caller-template declareren dit expliciet. Staat de
default `GITHUB_TOKEN` van de org op read-only, dan is de `permissions`-blok in
de caller (die de template al bevat) noodzakelijk.

## Volgorde van uitrol

De caller verwijst naar
`Impertio-Studio/.github/.github/workflows/release.yml@main`. Merge daarom eerst
deze workflow naar `main` in `Impertio-Studio/.github`, en pas daarna de callers
in de losse repos. Een caller die eerder live gaat, faalt omdat de herbruikbare
workflow op `main` nog niet bestaat.
