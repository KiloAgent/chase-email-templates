---
name: chase-email-templates
description: Use this when writing a follow-up email for a missing document, overdue invoice, unsigned contract, or similar chase. Pick a scenario, fill the fields, choose the step by days overdue, and send only after the user approves.
license: MIT
metadata:
  author: KiloAgent
  version: "0.1.0"
---

# Chase-email templates

Twelve plain-text follow-up scenarios. Each file has three steps: first nudge, second reminder, final notice.

## Rules

1. Pick the scenario from [templates/](templates/). Use the table below.
2. Read that file. Fill every `{{field}}` from its front matter. Unknown fields are a hard error.
3. Choose the step from `cadence_days` and how many days have passed since the first send (day 0):
   - before the second number: Step 1
   - at or after the second number, before the third: Step 2
   - at or after the third number: Step 3
4. Show the filled Subject and Body to the user. Send through the user's own email tool only after the user approves that send.
5. Never send on your own. Never queue a later step. Ask again before Step 2 and before Step 3.

You can fill fields with `merge` from [scripts/merge.js](scripts/merge.js), or by substituting values yourself. After a fill, the text must have no leftover `{` or `}`. The same function is re-exported from the repo file `build/merge.js`.

## Scenarios

| File | Slug | Cadence (days) |
| --- | --- | --- |
| [templates/01-coi-chase.md](templates/01-coi-chase.md) | coi-chase | 0, 4, 9 |
| [templates/02-invoice-overdue.md](templates/02-invoice-overdue.md) | invoice-overdue | 0, 4, 9 |
| [templates/03-missing-document.md](templates/03-missing-document.md) | missing-document | 0, 4, 9 |
| [templates/04-contract-signature.md](templates/04-contract-signature.md) | contract-signature | 0, 3, 7 |
| [templates/05-quote-followup.md](templates/05-quote-followup.md) | quote-followup | 0, 4, 10 |
| [templates/06-appointment-confirmation.md](templates/06-appointment-confirmation.md) | appointment-confirmation | 0, 1, 2 |
| [templates/07-portal-access.md](templates/07-portal-access.md) | portal-access | 0, 3, 7 |
| [templates/08-approval-request.md](templates/08-approval-request.md) | approval-request | 0, 2, 5 |
| [templates/09-onboarding-info.md](templates/09-onboarding-info.md) | onboarding-info | 0, 3, 7 |
| [templates/10-delivery-status.md](templates/10-delivery-status.md) | delivery-status | 0, 2, 5 |
| [templates/11-review-request.md](templates/11-review-request.md) | review-request | 0, 5, 12 |
| [templates/12-meeting-reschedule.md](templates/12-meeting-reschedule.md) | meeting-reschedule | 0, 3, 7 |

Allowed fields are listed in [templates/_schema.json](templates/_schema.json). Each template names the subset it uses.

## Tone

- Step 1: friendly assumption of oversight
- Step 2: clear and specific
- Step 3: firm, polite, one concrete next step

Do not add threats, legal language, late-fee amounts, emoji, or the word URGENT. Keep the body at or under 120 words. Leave in what is needed, by when, how to send it, and a thank-you.

## Do not

- Send email or messages without the user's approval for that send
- Invent customer names, inboxes, or live IDs
- Mention pricing or a sales offer
- Give legal, tax, medical, or financial advice
- Use em dashes or en dashes in copy
- Put secrets in the filled draft

## Evals

[evals/evals.test.ts](evals/evals.test.ts). From the repo root: `npm test` or `npm run evals`. No network and no API keys. Case table: [evals/README.md](evals/README.md).

## Chat users

If there is no skills directory, paste [PASTE_IN.md](PASTE_IN.md) into the chat. The same file is at the repo root.
