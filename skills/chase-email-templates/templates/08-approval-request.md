---
slug: approval-request
title: Approval or decision needed
who_sends: project manager / operations / designer
who_receives: client, internal approver, manager
fields: [recipient_first_name, sender_name, sender_company, due_date, project_or_ref, document_name]
cadence_days: [0, 2, 5]
---
## Step 1: First nudge (day 0)
Subject: Approval needed: {{document_name}} for {{project_or_ref}}
Body:
Hi {{recipient_first_name}},

Could you review and approve {{document_name}} for {{project_or_ref}} by {{due_date}}? Reply "approved" or tell me what to change, and I'll move on right away.

Thanks,
{{sender_name}}, {{sender_company}}

## Step 2: Second reminder (day 2)
Subject: Reminder: approval for {{document_name}}
Body:
Hi {{recipient_first_name}},

I'm still waiting on your approval of {{document_name}} for {{project_or_ref}}. The next step is on hold until I hear from you. A one-word reply is enough.

Thank you,
{{sender_name}}, {{sender_company}}

## Step 3: Final notice (day 5)
Subject: Decision needed to keep {{project_or_ref}} on track
Body:
Hi {{recipient_first_name}},

Without a decision on {{document_name}} by {{due_date}}, I'll need to pause {{project_or_ref}} and update the timeline. Please reply "approved" or "hold", or tell me what you'd like changed.

Thank you,
{{sender_name}}, {{sender_company}}
