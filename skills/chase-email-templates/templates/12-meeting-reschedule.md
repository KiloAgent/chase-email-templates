---
slug: meeting-reschedule
title: No-show or unanswered reschedule
who_sends: sales / customer success / scheduler
who_receives: prospect, client, partner
fields: [recipient_first_name, sender_name, sender_company, due_date, project_or_ref]
cadence_days: [0, 3, 7]
---
## Step 1: First nudge (day 0)
Subject: Let's find a new time for {{project_or_ref}}
Body:
Hi {{recipient_first_name}},

We missed each other for {{project_or_ref}} on {{due_date}}, no problem. Could you suggest two times that work for you over the next week? I'll confirm one right away.

Thanks,
{{sender_name}}, {{sender_company}}

## Step 2: Second reminder (day 3)
Subject: Still keen to meet about {{project_or_ref}}
Body:
Hi {{recipient_first_name}},

I'd still like to find a time for {{project_or_ref}}. If it's easier, reply with two windows that suit you and I'll fit in around them.

Thank you,
{{sender_name}}, {{sender_company}}

## Step 3: Final notice (day 7)
Subject: Should I close this out?
Body:
Hi {{recipient_first_name}},

I haven't been able to find a time for {{project_or_ref}}, so I'll close this on my side. If now isn't the right moment, reply "later" and I'll check back next month. If you'd like to meet, reply with a time that works.

All the best,
{{sender_name}}, {{sender_company}}
