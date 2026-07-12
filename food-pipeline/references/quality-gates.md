# Quality Gates — criteria per stage

The checklist `quality_gate` applies between stages. Each gate returns
**proceed / revise / stop** with evidence per criterion.

## After RESEARCH — evidence sufficiency
- [ ] Each research question is addressed by appraised, prioritized sources.
- [ ] Sources validated (exist, not retracted, not predatory) and tiered by journal ranking.
- [ ] No fatal coverage gap; coverage bias disclosed.
- Fail → back to RESEARCH.

## After WRITE — integrity + journal compliance
- [ ] **Integrity:** numbers in text match tables/figures; every claim traces to a result or a cited source; no fabrication; stats reported fully.
- [ ] **Reproducibility:** Methods reproducible (source, prep, storage, instrument settings); data/code availability stated.
- [ ] **Journal compliance:** structure, word/abstract limits, reference style, display-item count match the target journal (or APA 7.0 default).
- Fail → back to WRITE.

## After REVIEW — mandatory author decision
- Present the panel's decision (Accept / Minor / Major / Reject) and prioritized concerns.
- **The author decides** which concerns to address. The pipeline does not decide this.

## After REVISE / RE-REVIEW — resolution
- [ ] Each accepted concern is actually resolved (point-by-point).
- [ ] No new issue introduced.
- Accept → FINALIZE; else one more loop (cap 2).

## Before FINALIZE — final compliance
- [ ] Every citation resolves (four-gate); reference style correct and consistent.
- [ ] All declarations present (competing interests, funding, CRediT, data availability, ethics).
- [ ] Format matches the target journal; figures at journal spec.
- [ ] **Privacy scan clean** — no local paths, machine/temp paths, secrets, or private data in the deliverable (`python3 scripts/privacy_scan.py <file>`; see `food-paper/references/privacy-and-confidentiality.md`).

## Non-negotiable
Integrity and ethics gates cannot be waived. A must-fix cannot be passed through.
