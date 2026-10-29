# Business Requirements Document: Customer And Business Onboarding (KYC And KYB)

| Item | Detail |
| --- | --- |
| Product | Kasi Wallet (fictional), a South African payments app for individuals and small businesses |
| Channels | Mobile app and WhatsApp |
| Version | 1.0 |
| Author | Lusanda Nongogo, Business Analyst |
| Status | Approved for build |

## 1. Background

Kasi Wallet lets people and small businesses send money, pay merchants and withdraw cash. Today onboarding is semi manual: customers upload documents, an operations agent checks them by hand and the customer waits one to three days. 41% of people who start onboarding never finish, and the manual queue is the main cost in the operations team.

As an accountable institution under the Financial Intelligence Centre Act (FICA), Kasi Wallet must identify and verify customers, screen them against sanctions lists, assess money laundering risk and keep records. Any redesign has to keep those controls intact while removing friction.

## 2. Objectives

| ID | Objective | Measure | Target |
| --- | --- | --- | --- |
| OB-01 | Faster onboarding | Median time from start to approved, individuals | Under 10 minutes |
| OB-02 | Fewer drop offs | Share of started applications that complete | From 59% to 75% |
| OB-03 | Less manual work | Share of applications sent to manual review | Under 15% |
| OB-04 | Compliance intact | Applications approved without sanctions screening or ID verification | Zero |
| OB-05 | Business customers | Median time to approve a small business | Under 2 working days |

## 3. Scope

**In scope**
- Individual onboarding (KYC) for South African ID holders
- Business onboarding (KYB) for sole proprietors and private companies registered with CIPC
- Identity verification against the Department of Home Affairs via an accredited verification provider
- Selfie liveness and face match
- Sanctions and PEP screening at onboarding
- Customer risk rating and tiered limits
- Manual review queue for exceptions
- Record keeping and audit trail

**Out of scope**
- Foreign nationals and asylum seekers (phase 2)
- Trusts, partnerships and non profit organisations (phase 2)
- Ongoing transaction monitoring (separate project)
- Periodic review and refresh of existing customers

## 4. Stakeholders

| Stakeholder | Interest | Role in this project |
| --- | --- | --- |
| Head of Product | Conversion and growth | Sponsor, signs off scope |
| Money Laundering Reporting Officer (MLRO) | FICA compliance, RMCP | Approves controls and risk rating |
| Operations lead | Manual review workload | Owns the review queue, UAT participant |
| Engineering lead | Feasibility, vendors | Builds and integrates |
| Customer support | Customer complaints | UAT participant |
| Verification and screening vendors | Integration | Provide APIs and test data |

## 5. Regulatory Context

- **FICA and the RMCP.** Kasi Wallet must follow its Risk Management and Compliance Programme, which sets out how it identifies, verifies and risk rates customers. FICA takes a risk based approach, so verification can be lighter for low risk customers and must be enhanced for high risk ones.
- **Targeted financial sanctions.** Every customer and, for businesses, every director and beneficial owner must be screened against the sanctions lists published by the Financial Intelligence Centre before the relationship starts.
- **Prominent persons.** FICA requires extra checks for domestic prominent influential persons and foreign prominent public officials, their family members and close associates. Foreign officials require senior management approval.
- **Beneficial ownership.** For companies, the natural persons who own or control the business must be identified. The design uses 5% ownership, in line with the CIPC beneficial ownership register.
- **POPIA.** Only the personal information needed for onboarding is collected, consent is captured, and ID images and biometrics are stored securely with defined retention.
- **Record keeping.** Records of identification and verification must be kept for at least five years after the relationship ends.

Regulatory references should be confirmed with the MLRO against the current RMCP and FIC guidance before build.

## 6. Business Requirements

Priority uses MoSCoW: Must, Should, Could, Won't (this release).

### Individual Onboarding

| ID | Requirement | Priority |
| --- | --- | --- |
| BR-01 | The customer must be able to start onboarding with a mobile number and a one time PIN. | Must |
| BR-02 | The system must capture the customer's SA ID number, full names and date of birth, and validate the ID number format and check digit before submission. | Must |
| BR-03 | The system must verify the ID number, names and date of birth against Home Affairs records through the verification provider. | Must |
| BR-04 | The system must reject applications where Home Affairs reports the person as deceased. | Must |
| BR-05 | The customer must complete a selfie liveness check, and the selfie must be matched against the Home Affairs photo. | Must |
| BR-06 | The system must allow up to three selfie attempts before routing the application to manual review. | Must |
| BR-07 | The system must capture a residential address. Proof of address documents must only be requested for customers rated high risk. | Should |
| BR-08 | The system must capture consent to process personal information in line with POPIA before any verification call is made. | Must |

### Business Onboarding

| ID | Requirement | Priority |
| --- | --- | --- |
| BR-09 | The system must look up a company's registration number at CIPC and confirm its name and active status. | Must |
| BR-10 | The system must retrieve the company's directors and require the applicant to be a director or provide a signed mandate. | Must |
| BR-11 | The applicant must declare all beneficial owners holding 5% or more, and each must be identified and verified as an individual. | Must |
| BR-12 | Sole proprietors must be onboarded as individuals with a business profile, without CIPC checks. | Should |
| BR-13 | The system must capture the nature of the business and expected monthly turnover. | Must |

### Screening, Risk And Decision

| ID | Requirement | Priority |
| --- | --- | --- |
| BR-14 | Every individual, director and beneficial owner must be screened against sanctions and PEP lists before approval. | Must |
| BR-15 | A potential sanctions match must block the application until a compliance analyst clears or confirms it. A confirmed match must be escalated to the MLRO and the customer must not be told why. | Must |
| BR-16 | A PEP match must place the customer in the high risk tier and require enhanced due diligence, including source of funds. Foreign officials must also require senior management approval. | Must |
| BR-17 | The system must calculate a customer risk rating from defined factors (see the risk rating model) and assign a low, medium or high tier. | Must |
| BR-18 | Each tier must have transaction and balance limits, set by the MLRO. | Must |
| BR-19 | Applications that pass all checks with a low or medium rating must be approved automatically. | Must |
| BR-20 | Applications that fail a check must show the customer a clear next step and must never reveal screening results. | Must |

### Operations And Audit

| ID | Requirement | Priority |
| --- | --- | --- |
| BR-21 | Exceptions must go to a manual review queue showing the reason, evidence and a service level timer. | Must |
| BR-22 | Reviewers must record a decision and reason. A reviewer must not be able to approve their own application or one they submitted. | Must |
| BR-23 | Every verification call, screening result, rating and decision must be logged with a timestamp and user, and retained for at least five years. | Must |
| BR-24 | Customers must be able to resume an incomplete application within 30 days without re-entering verified data. | Should |
| BR-25 | The operations lead must see a daily dashboard of applications by status, drop off step and queue age. | Could |
| BR-26 | Onboarding of foreign nationals. | Won't |

## 7. Non Functional Requirements

| ID | Requirement |
| --- | --- |
| NFR-01 | Automated decisions for individuals within 2 minutes of the final submission, 95% of the time |
| NFR-02 | ID images and biometrics encrypted at rest and in transit, accessible only to roles that need them |
| NFR-03 | Onboarding usable on low end Android devices and on a 3G connection |
| NFR-04 | Content available in English, isiZulu and isiXhosa |
| NFR-05 | Vendor outages must queue the application for retry, not fail it |

## 8. Assumptions, Constraints And Risks

**Assumptions**
- The verification provider returns the Home Affairs photo for face matching.
- The screening provider updates sanctions lists within 24 hours of FIC publication.

**Constraints**
- Vendor costs are charged per call, so checks must run in an order that avoids paying for verification on applications that will fail cheaper checks.
- The MLRO must approve the risk rating model before go live.

**Risks**

| Risk | Impact | Mitigation |
| --- | --- | --- |
| High false match rate on common names in screening | Long queues, angry customers | Match on date of birth and ID number as well as name; tune fuzzy match threshold in UAT |
| Liveness check fails on low end cameras | Drop off, unfair exclusion | Three attempts, then manual review; test on low end devices in UAT |
| Vendor downtime | Applications stuck | Retry queue (NFR-05) and status messages to the customer |

## 9. Success Measures After Launch

Tracked weekly for the first three months: completion rate (OB-02), median time to approve (OB-01), manual review share (OB-03), screening alerts per 1 000 applications, and any application approved without a full check (OB-04, must stay at zero).
