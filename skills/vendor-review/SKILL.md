---
name: vendor-review
description: "Used for a monthly or on-demand review of the companies' vendors and subscriptions: who pays what, upcoming renewals, failed payments, duplicates and unused tools. Recommendations only."
license: MIT
---

# Company vendor review

A short monthly view of what the companies pay for, what renews soon, and what is failing.

## Inputs
- The vendor list in memory (vendor, purpose, paying entity, billing cycle, renewal date if known).
- New billing notices the assistant may read (forwarded or pasted receipts, failed-payment emails, a billing export). If none are connected, say so and use only memory plus what the owner posted.

## Steps
1. **Update the list** from new notices: new vendor, renewal date, failed payment, cancellation.
2. **Flag:** past-due or failed payments (with the consequence if stated, e.g. service suspension) first; renewals in the next 30 days; vendors with unclear paying entity; possible duplicates or tools with no recent use (inference; mark it).
3. **Propose** actions: update card, cancel, move to the other entity, ask the owner. Never act.
4. **Post:**
   ```
   Vendors & subscriptions — <month>
   Failing / past due: …
   Renewing in 30 days: …
   Entity to confirm: …
   Possible savings (inference): …
   ```

## Never
- Change payment methods, cancel, upgrade or pay.
- Store amounts, card details or account numbers in memory.
- Include personal subscriptions; if one appears, leave it out.
