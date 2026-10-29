# UAT Plan: Onboarding Release 1.0

## Purpose

Confirm that the new onboarding flow meets the business requirements in the BRD, keeps every FICA control in place, and works for real customers on real devices before it goes live.

## Scope

- All Must and Should requirements in the BRD (BR-01 to BR-25) and NFR-03 and NFR-05
- Individual and business onboarding on the mobile app
- Manual review queue and audit history in the operations portal

Out of scope: performance and load testing (done by engineering), penetration testing (separate security review), WhatsApp channel (UAT in release 1.1).

## Approach

- Test cases are written from the acceptance criteria in `docs/04_user_stories.md`, at least one per Must requirement. `scripts/uat_report.py` checks this.
- Vendor sandboxes provide test identities: a full match, a deceased record, a sanctions list entry, a domestic PEP and a foreign official.
- Each failure is logged in `uat/defect_log.csv` with steps to reproduce and classified as a bug, configuration issue, environment issue or usability concern, so engineering only receives real bugs.
- Fixed defects are retested by the tester who raised them.

## Roles

| Role | Person | Responsibility |
| --- | --- | --- |
| UAT lead | Business Analyst | Plan, test cases, defect triage, summary |
| Testers | Operations lead, two reviewers, support agent | Run test cases, raise defects |
| Compliance tester | Compliance analyst | Screening, PEP and audit cases |
| Defect fixes | Engineering lead | Fix, deploy to UAT, confirm |
| Sign off | Head of Product and MLRO | Go or no go decision |

## Entry Criteria

- Build deployed to UAT with release notes
- Vendor sandboxes connected and test identities confirmed
- Test cases reviewed by the operations lead and compliance analyst

## Exit Criteria

- Every Must requirement has at least one passed test case
- No open Critical defects
- No open High defects without an agreed workaround and fix date
- Compliance tester confirms screening, PEP handling and audit trail

## Severity Definitions

| Severity | Meaning |
| --- | --- |
| Critical | Compliance breach, data loss or no workaround for a core journey |
| High | Core journey broken for a group of customers, or a control weakened |
| Medium | Wrong behaviour with a workaround |
| Low | Cosmetic or minor inconvenience |

## Schedule

| Week | Activity |
| --- | --- |
| 1 | Test case review, environment checks, first run |
| 2 | Defect fixes and retest |
| 3 | Regression of fixed areas, summary and sign off meeting |
