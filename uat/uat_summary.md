# UAT Summary And Sign Off Recommendation

**Release:** Onboarding 1.0
**Prepared by:** Lusanda Nongogo, UAT lead
**Recommendation:** **No go** until three defects are closed (see below). Expected to move to go after one more fix and retest cycle.

## Results

| Measure | First run | After retest |
| --- | ---: | ---: |
| Test cases | 35 | 35 |
| Passed | 25 (71%) | 30 (86%) |
| Failed | 9 | 4 |
| Blocked | 1 | 1 |

All Must requirements have at least one test case. The coverage check found two gaps before the first run (BR-13 and BR-20), and test cases TC-34 and TC-35 were added.

## Defects

10 defects raised: 2 Critical, 4 High, 2 Medium, 2 Low. By type: 7 bugs, 1 configuration, 1 environment, 1 usability.

### Fixed And Retested

| ID | Severity | Issue |
| --- | --- | --- |
| DEF-06 | Critical | Decline SMS told the customer they failed sanctions screening, which tips off a possibly sanctioned person. Message replaced and all 14 customer messages reviewed (TC-35). |
| DEF-02 | High | Name mismatches were declined instead of reviewed, which would have turned away customers with spelling differences at Home Affairs. |
| DEF-05 | High | Business owners could continue with less than 100% of ownership declared, leaving beneficial owners unidentified. |
| DEF-09 | Medium | Risk tier boundary used greater than instead of greater or equal, so a 1.60 score was rated Low. |
| DEF-01 | Low | Date of birth was not checked against the ID number. |

### Still Open

| ID | Severity | Issue | Blocks go live? |
| --- | --- | --- | --- |
| DEF-03 | Critical | When the verification provider times out, the application is lost instead of queued for retry. | Yes |
| DEF-04 | High | Camera preview freezes on entry level Android phones over 3G, so liveness cannot be completed. This excludes the customers the product is built for. | Yes |
| DEF-08 | High | The senior management approval step for foreign officials is not deployed to UAT, so TC-23 could not run. | Yes, the control is untested |
| DEF-07 | Medium | Screening matches on name alone, raising false matches on common names. | No. Workaround: compliance clears manually. Tune before volume grows. |

### Deferred

DEF-10 (resume asks for the ID again) is a usability issue. Product agreed to fix it in release 1.1.

## What Went Well

- Every control the MLRO needs (consent before verification, sanctions block, PEP tiering, four eyes rule, audit trail) passed or has a defect being fixed.
- Classifying defects by type kept engineering focused: the configuration and environment issues went to the vendor and DevOps instead of the development backlog.

## Next Steps

1. Engineering to fix DEF-03 and DEF-04, DevOps to deploy the approval workflow for DEF-08.
2. Retest TC-09, TC-12 and TC-23, plus regression on the Home Affairs and liveness steps.
3. Compliance and vendor to tune screening on date of birth and ID number for DEF-07.
4. Reconvene sign off with the Head of Product and MLRO.
