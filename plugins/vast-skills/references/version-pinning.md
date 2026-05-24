# Reference version pinning

Plugin references in this directory are condensed extracts from framework canonical docs (paths relative to framework repo root).

## Current version

**Framework:** v3.4 (synced 2026-05-24).

**Last sync:** 2026-05-24

## Files and their canonical sources

| Plugin reference | Canonical source(s) |
|---|---|
| `vast-essentials.md` | `vast.md` (sections: "The four layers", "The triad", "What the composition framework actually owns — invariants vs implementations"), `glossary.md` ("Vocabulary aliases") |
| `layer-definitions.md` | `governance.md` ("Level 1 — Company", "Level 2 — Product", "Level 3 — Function") = primary source for company/product/function scope rows; `architecture-levels.md` = WoW scope + Architecture-row detail for product/function |
| `anti-patterns.md` | `anti-patterns.md` (the canonical catalogue — this companion is its doc-detectable subset, covering 8 of 13 `AP-NN`) |

Source is `glossary.md` (the canonical definitions doc). Extract definitions from there.

Skill-specific references in `skills/*/references/` are sourced as documented in each file's header.

## Regeneration

Current: manual. When framework version bumps, manually re-extract per the source map above.

Later: automated via `scripts/sync-refs.sh` (deferred — see design spec).

## Drift signal

If a finding from a skill cites framework content that differs from canonical, framework wins. Update plugin references and bump "Last sync" date.
