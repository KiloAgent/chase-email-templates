---
slug: missing-document
title: Missing required document
who_sends: operations / admin / onboarding
who_receives: client, vendor, applicant
fields: [recipient_first_name, sender_name, sender_company, due_date, project_or_ref, document_name]
cadence_days: [0, 4, 9]
---
## Step 1: First nudge (day 0)
Subject: {{document_name}} for {{project_or_ref}}
Body:
Hi {{recipient_first_name}},

To finish {{project_or_ref}} we still need your {{document_name}}. Could you send it by {{due_date}}? A scan or a clear photo as a reply to this email is fine.

Thanks a lot,
{{sender_name}}, {{sender_company}}

## Step 2: Second reminder (day 4)
Subject: Reminder: {{document_name}} for {{project_or_ref}}
Body:
Hi {{recipient_first_name}},

I haven't received your {{document_name}} for {{project_or_ref}} yet, and we need it by {{due_date}} to keep things moving. If you can't find it or aren't sure what we mean, tell me and I'll help you get it.

Thank you,
{{sender_name}}, {{sender_company}}

## Step 3: Final notice (day 9)
Subject: {{document_name}} needed to move forward with {{project_or_ref}}
Body:
Hi {{recipient_first_name}},

We can't complete {{project_or_ref}} until we have your {{document_name}}. Please send it today, or reply with the date it will reach us and I'll note it on our side.

Thank you,
{{sender_name}}, {{sender_company}}
