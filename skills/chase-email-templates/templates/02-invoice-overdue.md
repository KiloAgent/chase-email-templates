---
slug: invoice-overdue
title: Invoice overdue
who_sends: finance / owner / account manager
who_receives: customer, client
fields: [recipient_first_name, sender_name, sender_company, due_date, project_or_ref]
cadence_days: [0, 4, 9]
---
## Step 1: First nudge (day 0)
Subject: Invoice {{project_or_ref}}, due {{due_date}}
Body:
Hi {{recipient_first_name}},

A quick check on invoice {{project_or_ref}}, which was due on {{due_date}}. I may have missed a payment, so if it's already on its way, thank you and please ignore this. If not, could you let me know when we can expect it?

Thanks,
{{sender_name}}, {{sender_company}}

## Step 2: Second reminder (day 4)
Subject: Reminder: invoice {{project_or_ref}} is overdue
Body:
Hi {{recipient_first_name}},

Invoice {{project_or_ref}} is now past its due date of {{due_date}}. Please could you confirm the payment date, or tell me if anything on the invoice needs correcting so we can fix it right away.

Thank you,
{{sender_name}}, {{sender_company}}

## Step 3: Final notice (day 9)
Subject: Invoice {{project_or_ref}} still unpaid
Body:
Hi {{recipient_first_name}},

We still haven't received payment for invoice {{project_or_ref}} (due {{due_date}}). Please send payment, or reply today with a firm payment date. If there's a problem with the invoice, tell me what it is and I'll sort it out so this can be closed.

Regards,
{{sender_name}}, {{sender_company}}
