# User Stories And Acceptance Criteria

Stories are grouped by epic. Each traces to the business requirements in the BRD and to UAT cases in `uat/test_cases.csv`.

## Epic 1: Individual Verification

### US-01 Start Onboarding
**As a** new customer **I want** to start with just my phone number **so that** I can begin without paperwork.
Traces to: BR-01, BR-08

```gherkin
Scenario: Valid OTP
  Given I have entered a South African mobile number
  When I enter the correct one time PIN within 5 minutes
  Then I see the POPIA consent screen

Scenario: Consent is required before verification
  Given I am on the consent screen
  When I decline consent
  Then no verification call is made
  And I am told onboarding cannot continue without consent
```

### US-02 Enter And Validate My ID
**As a** new customer **I want** my ID number checked as I type **so that** I fix mistakes before submitting.
Traces to: BR-02

```gherkin
Scenario: Invalid check digit
  Given I enter a 13 digit ID number with a wrong check digit
  When I tap Continue
  Then I see "Please check your ID number" next to the field
  And the Home Affairs check is not called

Scenario: Date of birth does not match ID number
  Given my ID number starts with 950312
  When I enter a date of birth of 13 March 1995
  Then I see a message that the date of birth does not match the ID number
```

### US-03 Home Affairs Verification
**As a** compliance officer **I want** every ID verified against Home Affairs **so that** we know the person exists and the details are theirs.
Traces to: BR-03, BR-04, NFR-05

```gherkin
Scenario: Full match
  Given the ID number, names and date of birth match Home Affairs
  Then the application moves to the selfie step

Scenario: Person recorded as deceased
  Given Home Affairs returns a deceased status
  Then the application is declined
  And the customer sees a general message with the support number

Scenario: Name mismatch
  Given the surname does not match Home Affairs
  Then the application goes to manual review with reason "Name mismatch"

Scenario: Vendor unavailable
  Given the verification provider does not respond within 30 seconds
  Then the application is queued for retry
  And the customer sees "We are still checking your details"
```

### US-04 Selfie And Liveness
**As a** compliance officer **I want** a live selfie matched to the Home Affairs photo **so that** nobody can onboard with someone else's ID.
Traces to: BR-05, BR-06, NFR-03

```gherkin
Scenario: Liveness passed and face matched
  Given I complete the liveness prompts
  And the face match score is above the threshold
  Then I move to screening

Scenario: Three failed attempts
  Given I have failed the liveness check twice
  When I fail a third time
  Then my application goes to manual review with reason "Liveness failed"
  And I am told a person will review it within one working day
```

## Epic 2: Business Verification

### US-05 Verify My Company
**As a** business owner **I want** my company found from its registration number **so that** I do not upload documents.
Traces to: BR-09, BR-10

```gherkin
Scenario: Active company and applicant is a director
  Given I enter a registration number in the format 2019/123456/07
  And CIPC returns the company as active with me listed as a director
  Then I move to the beneficial owner step

Scenario: Deregistered company
  Given CIPC returns the company as deregistered
  Then the application is declined with the reason shown

Scenario: Applicant is not a director
  Given CIPC does not list me as a director
  Then I am asked to upload a signed mandate
  And the application goes to manual review
```

### US-06 Declare Beneficial Owners
**As a** compliance officer **I want** everyone who owns 5% or more identified **so that** we know who really controls the business.
Traces to: BR-11, BR-14

```gherkin
Scenario: Ownership adds up
  Given I declare owners whose shares total 100%
  Then each owner with 5% or more receives a link to verify their identity
  And each is screened for sanctions and PEP status

Scenario: Ownership does not add up
  Given the declared shares total less than 100%
  Then I cannot continue until I explain the remaining ownership
```

## Epic 3: Screening And Risk

### US-07 Sanctions Screening
**As the** MLRO **I want** possible sanctions matches blocked until reviewed **so that** we never onboard a sanctioned person.
Traces to: BR-14, BR-15, BR-20

```gherkin
Scenario: Possible match
  Given screening returns a possible match
  Then the application is blocked
  And it appears in the compliance queue with the matched list entry
  And the customer sees only "Your application is being reviewed"

Scenario: Confirmed match
  Given a compliance analyst confirms the match
  Then the application is declined
  And the case is escalated to the MLRO
  And the customer is not told the reason
```

### US-08 PEP Handling
**As the** MLRO **I want** PEPs placed in the high risk tier with enhanced checks **so that** we meet FICA requirements for prominent persons.
Traces to: BR-16

```gherkin
Scenario: Domestic prominent person
  Given screening identifies the customer as a domestic prominent influential person
  Then the risk tier is set to High
  And source of funds is requested

Scenario: Foreign official
  Given screening identifies a foreign prominent public official
  Then senior management approval is required before the account opens
```

### US-09 Risk Rating And Limits
**As an** operations lead **I want** low and medium risk customers approved automatically **so that** the team only handles real exceptions.
Traces to: BR-17, BR-18, BR-19

```gherkin
Scenario: Low risk customer
  Given all checks pass and the risk score is below 1.6
  Then the account is approved automatically
  And monthly and balance limits are set to R25 000

Scenario: High risk customer
  Given the risk score is 2.2 or above
  Then the application goes to manual review
  And proof of address and source of funds are requested
```

## Epic 4: Operations And Audit

### US-10 Manual Review Queue
**As a** reviewer **I want** one queue with the reason and evidence for each case **so that** I can decide quickly and consistently.
Traces to: BR-21, BR-22

```gherkin
Scenario: Reviewer decision
  Given I open a case in the queue
  Then I see the reason, the verification results and the time in queue
  When I approve or decline
  Then I must choose a reason from a list before saving

Scenario: Four eyes rule
  Given I submitted an application on behalf of a customer
  When I try to approve it
  Then the approve button is disabled
```

### US-11 Audit Trail
**As the** MLRO **I want** every check and decision logged **so that** we can show the regulator what happened.
Traces to: BR-23

```gherkin
Scenario: Full history
  Given an application has been approved
  When I open its audit history
  Then I see every vendor call, result, rating, decision, user and timestamp in order
```

### US-12 Resume Application
**As a** customer **I want** to continue where I stopped **so that** I do not start again.
Traces to: BR-24

```gherkin
Scenario: Resume within 30 days
  Given I verified my ID 10 days ago and stopped at the selfie step
  When I log in again
  Then I continue at the selfie step without re-entering my ID
```
