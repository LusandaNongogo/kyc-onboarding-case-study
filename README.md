# KYC And KYB Onboarding: Business Analysis Case Study

[![Tests](https://github.com/LusandaNongogo/kyc-onboarding-case-study/actions/workflows/tests.yml/badge.svg)](https://github.com/LusandaNongogo/kyc-onboarding-case-study/actions/workflows/tests.yml)

A complete business analysis and UAT pack for redesigning customer and business onboarding at **Kasi Wallet, a fictional South African payments app**. It takes the work from problem to sign off: requirements, process maps, risk rating, user stories, test cases, defects and a go or no go recommendation.

The company and all test data are made up. The regulatory context (FICA, sanctions screening, prominent persons, beneficial ownership, POPIA) is real.

## The Problem

Onboarding was manual: customers uploaded documents, an agent checked them by eye and searched sanctions lists by hand, and approval took one to three days. 41% of applicants never finished. The redesign had to cut that friction without weakening a single FICA control.

## What Is In The Pack

| Document | What it shows |
| --- | --- |
| [Business Requirements Document](docs/01_brd.md) | Objectives with targets, scope, stakeholders, regulatory context, 26 prioritised requirements, NFRs, risks |
| [Process Maps](docs/02_process_maps.md) | Current state with pain points, future state for individuals and businesses (rendered diagrams), swimlane roles |
| [Risk Rating Model](docs/03_risk_rating.md) | Weighted factors, tiers, limits, overrides and worked examples |
| [User Stories](docs/04_user_stories.md) | 12 stories across 4 epics with Gherkin acceptance criteria, traced to requirements |
| [UAT Plan](uat/test_plan.md) | Approach, roles, entry and exit criteria, severity definitions |
| [Test Cases](uat/test_cases.csv) | 35 cases traced to stories and requirements, with first run and retest results |
| [Defect Log](uat/defect_log.csv) | 10 defects with reproduction steps, severity and type |
| [UAT Summary](uat/uat_summary.md) | Results, open defects and the sign off recommendation |

## Key Decisions

- **Proof of address only for high risk customers.** It was the biggest drop off point, and a risk based approach under FICA does not require it for everyone.
- **Cheapest checks first.** Format checks, then Home Affairs, then liveness, then screening, so paid vendor calls are not wasted on applications that fail earlier.
- **Never tip off.** No customer message reveals screening results. UAT caught a decline SMS that did (DEF-06, Critical).
- **No go at sign off.** UAT ended at an 86% pass rate with three blocking defects, including one that excluded customers on entry level phones. The recommendation is no go until those are fixed.

## UAT Results

```
Test cases: 35
First run:    Pass 25, Fail 9, Blocked 1  (71%)
After retest: Pass 30, Fail 4, Blocked 1  (86%)
Defects: 10 (2 Critical, 4 High, 2 Medium, 2 Low)
Must requirements with no test case: none
```

This summary comes from `scripts/uat_report.py`, which also checks that every Must requirement in the BRD has at least one test case. On the first run it found two gaps, and the missing test cases were added.

## Run The Coverage Check (Windows)

```
py scripts/uat_report.py
py -m pip install pytest
py -m pytest
```
