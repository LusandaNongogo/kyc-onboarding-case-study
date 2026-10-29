# Customer Risk Rating Model

Supports BR-16, BR-17 and BR-18. To be approved by the MLRO before go live.

## Factors

Each factor scores 1 (low), 2 (medium) or 3 (high). The weighted total sets the tier.

| Factor | Weight | 1 | 2 | 3 |
| --- | ---: | --- | --- | --- |
| Customer type | 20% | Salaried individual | Sole proprietor | Private company |
| Nature of business | 25% | Retail, services, salaried | Cash intensive (spaza, taxi, salon) | Money services, second hand goods, crypto, gambling |
| Expected monthly turnover | 20% | Under R25 000 | R25 000 to R250 000 | Over R250 000 |
| Delivery channel | 15% | App with liveness passed | WhatsApp with liveness passed | Liveness failed, verified manually |
| Ownership complexity | 20% | Individual | One layer of company ownership | Owners are other companies or trusts |

**Score** = sum of (factor score x weight), giving a value from 1.0 to 3.0.

## Tiers

| Tier | Score | Monthly limit | Balance limit | Due diligence |
| --- | --- | --- | --- | --- |
| Low | Under 1.6 | R25 000 | R25 000 | Standard, no proof of address |
| Medium | 1.6 to under 2.2 | R100 000 | R100 000 | Standard |
| High | 2.2 and above | Set per customer | Set per customer | Enhanced: source of funds, proof of address, manual approval |

Limits are illustrative and are set by the MLRO.

## Overrides

These place a customer in the high tier whatever the score:

- PEP, family member or close associate match
- Business in a sector the RMCP lists as high risk
- Beneficial owner who could not be verified

A confirmed sanctions match is not a risk tier. The application is declined and escalated (BR-15).

## Worked Examples

| Customer | Factors (score) | Weighted score | Tier |
| --- | --- | ---: | --- |
| Salaried nurse, app | Type 1, nature 1, turnover 1, channel 1, ownership 1 | 1.00 | Low |
| Spaza shop owner, sole proprietor, WhatsApp, R60 000 a month | Type 2, nature 2, turnover 2, channel 2, ownership 1 | 1.80 | Medium |
| Private company trading second hand goods, R400 000 a month, owned by a holding company | Type 3, nature 3, turnover 3, channel 1, ownership 2 | 2.50 | High |
| Salaried individual who is a domestic PEP | Score 1.00 | 1.00 | High (override) |

Check of the spaza example: 0.20 x 2 + 0.25 x 2 + 0.20 x 2 + 0.15 x 2 + 0.20 x 1 = 1.80.
Check of the company example: 0.20 x 3 + 0.25 x 3 + 0.20 x 3 + 0.15 x 1 + 0.20 x 2 = 2.50.
