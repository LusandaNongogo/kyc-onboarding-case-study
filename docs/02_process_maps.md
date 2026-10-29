# Process Maps

GitHub renders the diagrams below directly.

## Current State: Individual Onboarding

```mermaid
flowchart TD
    A[Customer downloads app] --> B[Enters details and uploads ID photo]
    B --> C[Uploads proof of address]
    C --> D[Application waits in shared inbox]
    D --> E{Agent checks documents by hand}
    E -- Unclear or missing --> F[Agent emails customer]
    F --> B
    E -- Looks fine --> G[Agent searches sanctions list manually]
    G --> H{Possible match?}
    H -- Yes --> I[Forward to compliance by email]
    I --> J{Compliance decision}
    J -- Cleared --> K[Agent approves]
    J -- Confirmed --> L[Decline and escalate]
    H -- No --> K
    K --> M[Customer notified by SMS, 1 to 3 days later]
```

### Pain Points

| # | Step | Problem | Effect |
| --- | --- | --- | --- |
| P1 | Proof of address | Requested from everyone, although many customers have none in their own name | Largest single drop off point |
| P2 | Shared inbox | No queue order, no service levels | Waits of 1 to 3 days |
| P3 | Manual document check | ID photo checked by eye, not against Home Affairs | Fraud risk, inconsistent decisions |
| P4 | Manual sanctions search | Name only search, no audit trail | Compliance risk, misses on spelling variants |
| P5 | Email loops | Customer has no status visibility | Support calls, abandonment |

## Future State: Individual Onboarding

```mermaid
flowchart TD
    A[Mobile number and OTP] --> B[POPIA consent]
    B --> C[Enter SA ID number and names]
    C --> D{ID format and check digit valid?}
    D -- No --> C
    D -- Yes --> E[Home Affairs verification]
    E --> F{Match and alive?}
    F -- Deceased --> X[Decline]
    F -- Mismatch --> R[Manual review queue]
    F -- Match --> G[Selfie liveness and face match]
    G --> H{Passed within 3 attempts?}
    H -- No --> R
    H -- Yes --> I[Sanctions and PEP screening]
    I --> J{Result}
    J -- Possible sanctions match --> S[Compliance review, application blocked]
    J -- PEP match --> P[High risk tier, enhanced due diligence]
    J -- Clear --> K[Calculate risk rating]
    P --> K
    K --> L{Tier}
    L -- Low or medium --> M[Auto approve with tier limits]
    L -- High --> N[Request source of funds and proof of address]
    N --> R
    R --> O{Reviewer decision}
    O -- Approve --> M
    O -- Decline --> X
    S --> T{Cleared?}
    T -- Yes --> K
    T -- Confirmed --> U[Decline, escalate to MLRO, no reason given]
```

Checks run cheapest first (format check, then Home Affairs, then liveness, then screening), so paid vendor calls are not spent on applications that would fail earlier.

## Future State: Business Onboarding

```mermaid
flowchart TD
    A[Applicant onboarded as individual] --> B{Business type}
    B -- Sole proprietor --> C[Capture trading name, nature of business, turnover]
    C --> K[Risk rating]
    B -- Private company --> D[Enter CIPC registration number]
    D --> E{Found and active at CIPC?}
    E -- No --> X[Decline with reason]
    E -- Yes --> F[Retrieve directors]
    F --> G{Applicant is a director?}
    G -- No --> H[Upload signed mandate]
    H --> R[Manual review]
    G -- Yes --> I[Declare beneficial owners at 5% or more]
    I --> J[Verify and screen each director and owner]
    J --> L{All verified and clear?}
    L -- No --> R
    L -- Yes --> K
    K --> M{Tier}
    M -- Low or medium --> N[Approve business wallet]
    M -- High --> R
    R --> O{Reviewer decision}
    O -- Approve --> N
    O -- Decline --> X
```

## Roles (Swimlane View)

| Step | Customer | System | Vendor | Operations | Compliance |
| --- | :---: | :---: | :---: | :---: | :---: |
| Enter details and consent | X | | | | |
| Format checks | | X | | | |
| Home Affairs verification | | X | X | | |
| Liveness and face match | X | X | X | | |
| Sanctions and PEP screening | | X | X | | |
| Possible sanctions match | | | | | X |
| Risk rating and limits | | X | | | |
| Manual review | | | | X | |
| Enhanced due diligence approval | | | | | X |
