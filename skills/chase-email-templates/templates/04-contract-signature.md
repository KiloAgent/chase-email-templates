---
slug: contract-signature
title: Contract or proposal awaiting signature
who_sends: owner / sales / account manager
who_receives: client, partner, new hire
fields: [recipient_first_name, sender_name, sender_company, due_date, project_or_ref, document_name]
cadence_days: [0, 3, 7]
---
## Step 1: First nudge (day 0)
Subject: {{document_name}} ready for your signature
Body:
Hi {{recipient_first_name}},

I sent {{document_name}} for {{project_or_ref}} over for your signature. Could you sign it by {{due_date}}? It only takes a couple of minutes. If anything needs changing, tell me and I'll update it.

Thanks,
{{sender_name}}, {{sender_company}}

## Step 2: Second reminder (day 3)
Subject: Reminder: {{document_name}} is still unsigned
Body:
Hi {{recipient_first_name}},

Just checking in on {{document_name}} for {{project_or_ref}}, which is still waiting for your signature. If a question or a change is holding it up, reply here and I'll sort it out quickly.

Thank you,
{{sender_name}}, {{sender_company}}

## Step 3: Final notice (day 7)
Subject: Still want to go ahead with {{project_or_ref}}?
Body:
Hi {{recipient_first_name}},

We can't start {{project_or_ref}} until {{document_name}} is signed, and I'll need to release the time we reserved for you after {{due_date}}. If you'd like to go ahead, please sign today. If plans have changed, a quick note is all I need.

Thank you,
{{sender_name}}, {{sender_company}}
