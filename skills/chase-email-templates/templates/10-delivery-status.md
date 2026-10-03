---
slug: delivery-status
title: Supplier delivery status unconfirmed
who_sends: purchasing / operations / project manager
who_receives: supplier, vendor, freight contact
fields: [recipient_first_name, sender_name, sender_company, due_date, project_or_ref]
cadence_days: [0, 2, 5]
---
## Step 1: First nudge (day 0)
Subject: Status of order {{project_or_ref}}
Body:
Hi {{recipient_first_name}},

Could you confirm the ship date and tracking for order {{project_or_ref}}? We were expecting it by {{due_date}}.

Thanks,
{{sender_name}}, {{sender_company}}

## Step 2: Second reminder (day 2)
Subject: Reminder: status of order {{project_or_ref}}
Body:
Hi {{recipient_first_name}},

I'm still missing a confirmed ship date for order {{project_or_ref}}, which was due {{due_date}}. Even a rough date or a note on what's delaying it would help us plan.

Thank you,
{{sender_name}}, {{sender_company}}

## Step 3: Final notice (day 5)
Subject: Firm delivery date needed for order {{project_or_ref}}
Body:
Hi {{recipient_first_name}},

I need a firm delivery date for order {{project_or_ref}} today. Without one, I'll have to make other arrangements for our customer. If something is blocking the shipment, tell me what it is and we can work through it.

Thank you,
{{sender_name}}, {{sender_company}}
