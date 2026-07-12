# OHAT Risk-of-Bias Tool — reference (incl. in vitro criteria)

The NTP/OHAT Risk-of-Bias tool used by `risk_of_bias` for **in vitro, human, and
animal** studies. Assessment is **outcome-specific** (rate per outcome, not once
per study). Source: NTP/OHAT, *Extending a Risk-of-Bias Approach to Address In
Vitro Studies* (A. Rooney, 2015) and the OHAT RoB tool/handbook
(http://ntp.niehs.nih.gov/go/38673).

## The 11 questions (6 bias domains)
| Domain | # | Question |
|---|---|---|
| Selection | 1 | Was administered dose / exposure level adequately randomized? |
| Selection | 2 | Was allocation to study groups adequately concealed? |
| Selection | 3 | Did selection of study participants result in appropriate comparison groups? |
| Confounding | 4 | Did study design or analysis account for important confounding and modifying variables? |
| Performance | 5 | Were experimental conditions identical across study groups? |
| Performance | 6 | Were research personnel blinded to the study group during the study? |
| Attrition/exclusion | 7 | Were outcome data complete without attrition or exclusion from analysis? |
| Detection | 8 | Can we be confident in the exposure characterization? |
| Detection | 9 | Can we be confident in the outcome assessment (incl. blinding of assessors)? |
| Selective reporting | 10 | Were all measured outcomes reported? |
| Other | 11 | Were there no other potential threats to internal validity? |

Q8 (exposure characterization) and Q9 (outcome assessment) are treated as the
tier-1 **key** questions.

## Rating scale (per question, per outcome)
`++` Definitely low · `+` Probably low · `−` Probably high · `−−` Definitely high
risk of bias. `NR` (not reported) is generally rated probably/definitely high when
the omission implies a bias risk. Justify each rating from the study report.

## Applicability by study design (which questions apply)
Study design determines which questions are answered.
- **In vitro exposure:** apply **Q1, Q2, Q5, Q6, Q7, Q8, Q9, Q10, Q11**. **Q3 and Q4 are Not Applicable** to in vitro studies.
- **Experimental animal:** Q1, Q2, Q4, Q5, Q6, Q7, Q8, Q9, Q10, Q11.
- **Human controlled exposure:** Q1, Q2, Q4, Q6, Q7, Q8, Q9, Q10, Q11.
- **Human observational (cohort / case-control / cross-sectional):** Q3, Q4, Q7, Q8, Q9, Q10, Q11 (design-dependent).
- **Case series:** Q7, Q8, Q9, Q10, Q11.

## In vitro–specific criteria (how to answer each applicable question)
Adapted from the experimental-animal criteria for in vitro exposure regimens:
- **Q1 Randomization** — In a **homogeneous cell suspension** there is no variation between groups, so randomization has no impact (not a source of bias). Where cells/tissues differ across groups, each should have an equal chance of assignment to any group, including controls.
- **Q2 Allocation concealment** — Same logic: with a homogeneous suspension there is no variation, so concealment has no impact. Otherwise, concealment of group assignment applies.
- **Q3 Participant selection** — **Not applicable** to in vitro.
- **Q4 Confounding** — **Not applicable** to in vitro.
- **Q5 Experimental conditions identical** — controls and experimental wells use the **same media**; the **same solvent/vehicle** is used for control cells; culture plates are **uniformly incubated and handled** (same medium and schedule for changes/washes, same time out of incubator, same incubator, and control for plate-location and plate-edge effects).
- **Q6 Blinding of personnel** — automated/**robotic systems eliminate the need**; otherwise blinding of personnel may apply.
- **Q7 Incomplete outcome data (attrition)** — account for **well or plate loss**; unexplained loss without explanation raises risk.
- **Q8 Exposure characterization** — confidence in the **purity, stability, solubility, and volatility** of the test substance.
- **Q9 Outcome assessment** — acceptable/well-established measurement methods and blinding of assessors, **unless automated with no handling** between exposure and measurement.
- **Q10 All outcomes reported** — whether all measured outcomes were reported.
- **Q11 Other threats** — project-specific issues (e.g., **appropriate statistical methods**).

## Output
Per-study table (rows = studies, columns = applicable questions with ++/+/−/−−
and a one-line justification), domain roll-ups, and an across-study heat table
highlighting the key questions (Q8, Q9).
