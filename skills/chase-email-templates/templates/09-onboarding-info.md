---
slug: onboarding-info
title: Onboarding details not returned
who_sends: onboarding / customer success / operations
who_receives: new client, new vendor, new team member
fields: [recipient_first_name, sender_name, sender_company, due_date, project_or_ref, document_name]
cadence_days: [0, 3, 7]
---
## Step 1: First nudge (day 0)
Subject: Next step to get started: {{document_name}}
Body:
Hi {{recipient_first_name}},

Welcome aboard. To get {{project_or_ref}} started, we need your {{document_name}} back by {{due_date}}. It should take about ten minutes. Reply here if any question stops you.

Looking forward to it,
{{sender_name}}, {{sender_company}}

## Step 2: Second reminder (day 3)
Subject: Reminder: {{document_name}} for {{project_or_ref}}
Body:
Hi {{recipient_first_name}},

I haven't received your {{document_name}} yet. We need it to set up {{project_or_ref}}. If it's easier, reply with the details in the email itself and I'll fill in the rest.

Thanks,
{{sender_name}}, {{sender_company}}

## Step 3: Final notice (day 7)
Subject: Your start date for {{project_or_ref}} depends on {{document_name}}
Body:
Hi {{recipient_first_name}},

We can't set a start date for {{project_or_ref}} without your {{document_name}}, and our next openings are filling up. Please send it today, or reply and tell me what's in the way.

Thank you,
{{sender_name}}, {{sender_company}}
