---
slug: quote-followup
title: Quote sent, no reply
who_sends: sales / owner / estimator
who_receives: prospect, customer
fields: [recipient_first_name, sender_name, sender_company, due_date, project_or_ref, document_name]
cadence_days: [0, 4, 10]
---
## Step 1: First nudge (day 0)
Subject: Following up on our quote for {{project_or_ref}}
Body:
Hi {{recipient_first_name}},

I wanted to check that you received our quote ({{document_name}}) for {{project_or_ref}}. I'm happy to walk you through it or adjust the scope. The quote is valid until {{due_date}}.

Best,
{{sender_name}}, {{sender_company}}

## Step 2: Second reminder (day 4)
Subject: Any questions on the quote for {{project_or_ref}}?
Body:
Hi {{recipient_first_name}},

Do you have any questions about the quote for {{project_or_ref}}? If it's price, scope or timing, tell me which and I'll see what I can do. Even a quick yes, no or not now helps me plan.

Thanks,
{{sender_name}}, {{sender_company}}

## Step 3: Final notice (day 10)
Subject: Closing the loop on {{project_or_ref}}
Body:
Hi {{recipient_first_name}},

I'll assume the timing isn't right and close this quote on my side after {{due_date}}, when it expires. If that changes, just reply and I'll refresh it for you.

All the best,
{{sender_name}}, {{sender_company}}
