---
slug: coi-chase
title: Certificate of insurance (COI) chase
who_sends: operations / project manager
who_receives: subcontractor, vendor, tenant
fields: [recipient_first_name, sender_name, sender_company, due_date, project_or_ref]
cadence_days: [0, 4, 9]
---
## Step 1: First nudge (day 0)
Subject: Certificate of insurance for {{project_or_ref}}
Body:
Hi {{recipient_first_name}},

We don't have a current certificate of insurance on file for {{project_or_ref}}. Could you send it over by {{due_date}}? A PDF reply to this email is perfect.

Thanks so much,
{{sender_name}}, {{sender_company}}

## Step 2: Second reminder (day 4)
Subject: Reminder: certificate of insurance for {{project_or_ref}}
Body:
Hi {{recipient_first_name}},

Following up on my note from earlier this week: we still need your certificate of insurance for {{project_or_ref}}, due {{due_date}}. If your broker issues it, forwarding this email to them is the fastest route.

Let me know if anything is blocking you.

Thanks,
{{sender_name}}, {{sender_company}}

## Step 3: Final notice (day 9)
Subject: Certificate of insurance needed to proceed with {{project_or_ref}}
Body:
Hi {{recipient_first_name}},

We haven't received the certificate of insurance for {{project_or_ref}}, and we're not able to schedule or pay for work until we have it. If it's on its way, reply with the date and I'll hold your slot. Otherwise, please send it today.

Thank you,
{{sender_name}}, {{sender_company}}
