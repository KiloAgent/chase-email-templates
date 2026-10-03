---
slug: portal-access
title: Access or login promised but not granted
who_sends: operations / project manager / bookkeeper
who_receives: client, vendor, IT contact
fields: [recipient_first_name, sender_name, sender_company, due_date, project_or_ref]
cadence_days: [0, 3, 7]
---
## Step 1: First nudge (day 0)
Subject: Access to {{project_or_ref}}
Body:
Hi {{recipient_first_name}},

Thanks for agreeing to give us access to {{project_or_ref}}. Could you set it up by {{due_date}}? Read-only access is fine. Please use the portal's own invite feature rather than sharing a password by email. Tell me if you need anything from us.

Thanks,
{{sender_name}}, {{sender_company}}

## Step 2: Second reminder (day 3)
Subject: Reminder: access to {{project_or_ref}}
Body:
Hi {{recipient_first_name}},

I still can't get into {{project_or_ref}}. If it needs approval from an admin or your IT team, tell me who to contact and I'll reach out to them directly.

Thank you,
{{sender_name}}, {{sender_company}}

## Step 3: Final notice (day 7)
Subject: Access to {{project_or_ref}} needed to continue
Body:
Hi {{recipient_first_name}},

The work that depends on {{project_or_ref}} is on hold until we have access. Please send the invite today, or tell me who can, and I'll follow up with them myself.

Thank you,
{{sender_name}}, {{sender_company}}
