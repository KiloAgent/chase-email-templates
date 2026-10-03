---
slug: appointment-confirmation
title: Appointment or visit confirmation
who_sends: front desk / scheduler / field operations
who_receives: customer, client
fields: [recipient_first_name, sender_name, sender_company, due_date, project_or_ref]
cadence_days: [0, 1, 2]
---
## Step 1: First nudge (day 0)
Subject: Please confirm: {{project_or_ref}} on {{due_date}}
Body:
Hi {{recipient_first_name}},

This is a quick request to confirm {{project_or_ref}} on {{due_date}}. Reply YES to confirm, or suggest another time and I'll rebook it.

Thanks,
{{sender_name}}, {{sender_company}}

## Step 2: Second reminder (day 1)
Subject: Reminder: please confirm {{project_or_ref}}
Body:
Hi {{recipient_first_name}},

I haven't heard back about {{project_or_ref}} on {{due_date}}, and I'm holding the slot for you. Reply YES to keep it. If it no longer works, tell me and we'll find another time.

Thank you,
{{sender_name}}, {{sender_company}}

## Step 3: Final notice (day 2)
Subject: We'll release your slot for {{due_date}} unless we hear back
Body:
Hi {{recipient_first_name}},

We'll release the slot for {{project_or_ref}} on {{due_date}} if we don't hear from you today. Reply YES to keep it, or tell me a better time and I'll rebook you.

Thank you,
{{sender_name}}, {{sender_company}}
