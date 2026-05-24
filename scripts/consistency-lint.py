#!/usr/bin/env python3
"""VAST release-consistency lint.

Mechanical checks a human shouldn't have to eyeball every release. The
judgment-level checks (term *meaning*, logic contradictions) stay human — see
anti-patterns.md. This guards the surface that drifts: links, IDs, counts, indices.

Checks:
  1. links     [error]  every relative markdown link resolves
  2. ap-ids    [error]  every AP-NN reference is defined in anti-patterns.md
  3. principle [error]  every "Principle N" is within kernel.md's set
  4. counts    [warn]   recurring canonical counts agree (anti-patterns / themes / principles)
  5. index     [warn]   every root doc is referenced from README or README-full

Exit 1 on any error-level finding, else 0. Excludes thinking/ (design scratch).
Run from anywhere — repo root is resolved from this file's location. Stdlib only.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ALL_MD = [p for p in ROOT.rglob("*.md") if ".git" not in p.parts]
PUBLISHED = [p for p in ALL_MD if "thinking" not in p.relative_to(ROOT).parts]

errors, warnings = [], []
def rel(p):
    return p.relative_to(ROOT)

# 1. link integrity (published docs only)
LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
def skippable(url):
    return (url.startswith(("http://", "https://", "mailto:", "#", "/"))
            or url.startswith("{") or "<" in url or "NNN" in url or "*" in url)
for p in PUBLISHED:
    for raw in LINK.findall(p.read_text(encoding="utf-8")):
        raw = raw.strip()
        url = raw.split()[0] if raw else ""        # drop optional "title"
        target = url.split("#", 1)[0]              # drop anchor
        if not target or skippable(target):
            continue
        if not (p.parent / target).exists():
            errors.append(("links", f"{rel(p)} -> broken link: {target}"))

# 2. AP-ID integrity
ap_text = (ROOT / "anti-patterns.md").read_text(encoding="utf-8")
defined = set(re.findall(r"^###\s+(AP-\d+)", ap_text, re.M))
if not defined:
    errors.append(("ap-ids", "anti-patterns.md defines no AP-NN headers"))
for p in PUBLISHED:
    for ref in sorted(set(re.findall(r"AP-\d+", p.read_text(encoding="utf-8")))):
        if ref not in defined:
            errors.append(("ap-ids", f"{rel(p)} -> undefined {ref} (defined: {len(defined)})"))

# 3. principle range
kernel = (ROOT / "kernel.md").read_text(encoding="utf-8")
n_principles = len(re.findall(r"^\d+\.\s+\*\*", kernel, re.M))
if n_principles != 7:
    warnings.append(("counts", f"kernel.md defines {n_principles} principles (expected 7)"))
ceiling = n_principles or 7
for p in PUBLISHED:
    for n in re.findall(r"Principle\s+(\d+)", p.read_text(encoding="utf-8")):
        if not 1 <= int(n) <= ceiling:
            errors.append(("principle", f"{rel(p)} -> Principle {n} out of range 1..{ceiling}"))

# 4. count guards
EXPECT = [(r"(\d+)\s+anti-patterns\b", 13, "anti-patterns"),
          (r"(\d+)\s+themes\b", 5, "themes"),
          (r"(\d+)\s+[Pp]rinciples\b", 7, "principles")]
for p in PUBLISHED:
    txt = p.read_text(encoding="utf-8")
    for rx, exp, label in EXPECT:
        for v in re.findall(rx, txt):
            if int(v) != exp:
                warnings.append(("counts", f"{rel(p)} -> says {v} {label} (expected {exp})"))

# 5. index coverage (root docs referenced from an index)
idx = (ROOT / "README.md").read_text(encoding="utf-8") + (ROOT / "README-full.md").read_text(encoding="utf-8")
for p in sorted(ROOT.glob("*.md")):
    if p.name in ("README.md", "README-full.md"):
        continue
    if p.name not in idx:
        warnings.append(("index", f"{p.name} -> root doc not referenced in README or README-full"))

# report
print("VAST consistency lint")
print("=" * 40)
print(f"scanned {len(ALL_MD)} md ({len(PUBLISHED)} published) · {len(defined)} AP-IDs · {n_principles} principles\n")
for label, items in (("ERRORS", errors), ("WARNINGS", warnings)):
    print(f"{label}: {len(items)}")
    for check, msg in items:
        print(f"  [{check}] {msg}")
    print()
print("RESULT:", "FAIL" if errors else "PASS")
sys.exit(1 if errors else 0)
