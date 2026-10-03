#!/usr/bin/env python3
"""Write the 12 chase-email templates. Source of truth for template copy."""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_DIR = os.path.join(ROOT, "skills", "chase-email-templates", "templates")
OUT_DIR = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_DIR

SIG = "{{sender_name}}, {{sender_company}}"
S = []


def sc(slug, title, who_sends, who_receives, fields, cad, steps):
    S.append(
        dict(
            slug=slug,
            title=title,
            who_sends=who_sends,
            who_receives=who_receives,
            fields=fields,
            cad=cad,
            steps=steps,
        )
    )


BASE = ["recipient_first_name", "sender_name", "sender_company", "due_date", "project_or_ref"]
DOC = BASE + ["document_name"]

sc(
    "coi-chase",
    "Certificate of insurance (COI) chase",
    "operations / project manager",
    "subcontractor, vendor, tenant",
    BASE,
    [0, 4, 9],
    [
        (
            "First nudge",
            "Certificate of insurance for {{project_or_ref}}",
            "We don't have a current certificate of insurance on file for {{project_or_ref}}. Could you send it over by {{due_date}}? A PDF reply to this email is perfect.\n\nThanks so much,",
        ),
        (
            "Second reminder",
            "Reminder: certificate of insurance for {{project_or_ref}}",
            "Following up on my note from earlier this week: we still need your certificate of insurance for {{project_or_ref}}, due {{due_date}}. If your broker issues it, forwarding this email to them is the fastest route.\n\nLet me know if anything is blocking you.\n\nThanks,",
        ),
        (
            "Final notice",
            "Certificate of insurance needed to proceed with {{project_or_ref}}",
            "We haven't received the certificate of insurance for {{project_or_ref}}, and we're not able to schedule or pay for work until we have it. If it's on its way, reply with the date and I'll hold your slot. Otherwise, please send it today.\n\nThank you,",
        ),
    ],
)

sc(
    "invoice-overdue",
    "Invoice overdue",
    "finance / owner / account manager",
    "customer, client",
    BASE,
    [0, 4, 9],
    [
        (
            "First nudge",
            "Invoice {{project_or_ref}}, due {{due_date}}",
            "A quick check on invoice {{project_or_ref}}, which was due on {{due_date}}. I may have missed a payment, so if it's already on its way, thank you and please ignore this. If not, could you let me know when we can expect it?\n\nThanks,",
        ),
        (
            "Second reminder",
            "Reminder: invoice {{project_or_ref}} is overdue",
            "Invoice {{project_or_ref}} is now past its due date of {{due_date}}. Please could you confirm the payment date, or tell me if anything on the invoice needs correcting so we can fix it right away.\n\nThank you,",
        ),
        (
            "Final notice",
            "Invoice {{project_or_ref}} still unpaid",
            "We still haven't received payment for invoice {{project_or_ref}} (due {{due_date}}). Please send payment, or reply today with a firm payment date. If there's a problem with the invoice, tell me what it is and I'll sort it out so this can be closed.\n\nRegards,",
        ),
    ],
)

sc(
    "missing-document",
    "Missing required document",
    "operations / admin / onboarding",
    "client, vendor, applicant",
    DOC,
    [0, 4, 9],
    [
        (
            "First nudge",
            "{{document_name}} for {{project_or_ref}}",
            "To finish {{project_or_ref}} we still need your {{document_name}}. Could you send it by {{due_date}}? A scan or a clear photo as a reply to this email is fine.\n\nThanks a lot,",
        ),
        (
            "Second reminder",
            "Reminder: {{document_name}} for {{project_or_ref}}",
            "I haven't received your {{document_name}} for {{project_or_ref}} yet, and we need it by {{due_date}} to keep things moving. If you can't find it or aren't sure what we mean, tell me and I'll help you get it.\n\nThank you,",
        ),
        (
            "Final notice",
            "{{document_name}} needed to move forward with {{project_or_ref}}",
            "We can't complete {{project_or_ref}} until we have your {{document_name}}. Please send it today, or reply with the date it will reach us and I'll note it on our side.\n\nThank you,",
        ),
    ],
)

sc(
    "contract-signature",
    "Contract or proposal awaiting signature",
    "owner / sales / account manager",
    "client, partner, new hire",
    DOC,
    [0, 3, 7],
    [
        (
            "First nudge",
            "{{document_name}} ready for your signature",
            "I sent {{document_name}} for {{project_or_ref}} over for your signature. Could you sign it by {{due_date}}? It only takes a couple of minutes. If anything needs changing, tell me and I'll update it.\n\nThanks,",
        ),
        (
            "Second reminder",
            "Reminder: {{document_name}} is still unsigned",
            "Just checking in on {{document_name}} for {{project_or_ref}}, which is still waiting for your signature. If a question or a change is holding it up, reply here and I'll sort it out quickly.\n\nThank you,",
        ),
        (
            "Final notice",
            "Still want to go ahead with {{project_or_ref}}?",
            "We can't start {{project_or_ref}} until {{document_name}} is signed, and I'll need to release the time we reserved for you after {{due_date}}. If you'd like to go ahead, please sign today. If plans have changed, a quick note is all I need.\n\nThank you,",
        ),
    ],
)

sc(
    "quote-followup",
    "Quote sent, no reply",
    "sales / owner / estimator",
    "prospect, customer",
    DOC,
    [0, 4, 10],
    [
        (
            "First nudge",
            "Following up on our quote for {{project_or_ref}}",
            "I wanted to check that you received our quote ({{document_name}}) for {{project_or_ref}}. I'm happy to walk you through it or adjust the scope. The quote is valid until {{due_date}}.\n\nBest,",
        ),
        (
            "Second reminder",
            "Any questions on the quote for {{project_or_ref}}?",
            "Do you have any questions about the quote for {{project_or_ref}}? If it's price, scope or timing, tell me which and I'll see what I can do. Even a quick yes, no or not now helps me plan.\n\nThanks,",
        ),
        (
            "Final notice",
            "Closing the loop on {{project_or_ref}}",
            "I'll assume the timing isn't right and close this quote on my side after {{due_date}}, when it expires. If that changes, just reply and I'll refresh it for you.\n\nAll the best,",
        ),
    ],
)

sc(
    "appointment-confirmation",
    "Appointment or visit confirmation",
    "front desk / scheduler / field operations",
    "customer, client",
    BASE,
    [0, 1, 2],
    [
        (
            "First nudge",
            "Please confirm: {{project_or_ref}} on {{due_date}}",
            "This is a quick request to confirm {{project_or_ref}} on {{due_date}}. Reply YES to confirm, or suggest another time and I'll rebook it.\n\nThanks,",
        ),
        (
            "Second reminder",
            "Reminder: please confirm {{project_or_ref}}",
            "I haven't heard back about {{project_or_ref}} on {{due_date}}, and I'm holding the slot for you. Reply YES to keep it. If it no longer works, tell me and we'll find another time.\n\nThank you,",
        ),
        (
            "Final notice",
            "We'll release your slot for {{due_date}} unless we hear back",
            "We'll release the slot for {{project_or_ref}} on {{due_date}} if we don't hear from you today. Reply YES to keep it, or tell me a better time and I'll rebook you.\n\nThank you,",
        ),
    ],
)

sc(
    "portal-access",
    "Access or login promised but not granted",
    "operations / project manager / bookkeeper",
    "client, vendor, IT contact",
    BASE,
    [0, 3, 7],
    [
        (
            "First nudge",
            "Access to {{project_or_ref}}",
            "Thanks for agreeing to give us access to {{project_or_ref}}. Could you set it up by {{due_date}}? Read-only access is fine. Please use the portal's own invite feature rather than sharing a password by email. Tell me if you need anything from us.\n\nThanks,",
        ),
        (
            "Second reminder",
            "Reminder: access to {{project_or_ref}}",
            "I still can't get into {{project_or_ref}}. If it needs approval from an admin or your IT team, tell me who to contact and I'll reach out to them directly.\n\nThank you,",
        ),
        (
            "Final notice",
            "Access to {{project_or_ref}} needed to continue",
            "The work that depends on {{project_or_ref}} is on hold until we have access. Please send the invite today, or tell me who can, and I'll follow up with them myself.\n\nThank you,",
        ),
    ],
)

sc(
    "approval-request",
    "Approval or decision needed",
    "project manager / operations / designer",
    "client, internal approver, manager",
    DOC,
    [0, 2, 5],
    [
        (
            "First nudge",
            "Approval needed: {{document_name}} for {{project_or_ref}}",
            'Could you review and approve {{document_name}} for {{project_or_ref}} by {{due_date}}? Reply "approved" or tell me what to change, and I\'ll move on right away.\n\nThanks,',
        ),
        (
            "Second reminder",
            "Reminder: approval for {{document_name}}",
            "I'm still waiting on your approval of {{document_name}} for {{project_or_ref}}. The next step is on hold until I hear from you. A one-word reply is enough.\n\nThank you,",
        ),
        (
            "Final notice",
            "Decision needed to keep {{project_or_ref}} on track",
            'Without a decision on {{document_name}} by {{due_date}}, I\'ll need to pause {{project_or_ref}} and update the timeline. Please reply "approved" or "hold", or tell me what you\'d like changed.\n\nThank you,',
        ),
    ],
)

sc(
    "onboarding-info",
    "Onboarding details not returned",
    "onboarding / customer success / operations",
    "new client, new vendor, new team member",
    DOC,
    [0, 3, 7],
    [
        (
            "First nudge",
            "Next step to get started: {{document_name}}",
            "Welcome aboard. To get {{project_or_ref}} started, we need your {{document_name}} back by {{due_date}}. It should take about ten minutes. Reply here if any question stops you.\n\nLooking forward to it,",
        ),
        (
            "Second reminder",
            "Reminder: {{document_name}} for {{project_or_ref}}",
            "I haven't received your {{document_name}} yet. We need it to set up {{project_or_ref}}. If it's easier, reply with the details in the email itself and I'll fill in the rest.\n\nThanks,",
        ),
        (
            "Final notice",
            "Your start date for {{project_or_ref}} depends on {{document_name}}",
            "We can't set a start date for {{project_or_ref}} without your {{document_name}}, and our next openings are filling up. Please send it today, or reply and tell me what's in the way.\n\nThank you,",
        ),
    ],
)

sc(
    "delivery-status",
    "Supplier delivery status unconfirmed",
    "purchasing / operations / project manager",
    "supplier, vendor, freight contact",
    BASE,
    [0, 2, 5],
    [
        (
            "First nudge",
            "Status of order {{project_or_ref}}",
            "Could you confirm the ship date and tracking for order {{project_or_ref}}? We were expecting it by {{due_date}}.\n\nThanks,",
        ),
        (
            "Second reminder",
            "Reminder: status of order {{project_or_ref}}",
            "I'm still missing a confirmed ship date for order {{project_or_ref}}, which was due {{due_date}}. Even a rough date or a note on what's delaying it would help us plan.\n\nThank you,",
        ),
        (
            "Final notice",
            "Firm delivery date needed for order {{project_or_ref}}",
            "I need a firm delivery date for order {{project_or_ref}} today. Without one, I'll have to make other arrangements for our customer. If something is blocking the shipment, tell me what it is and we can work through it.\n\nThank you,",
        ),
    ],
)

sc(
    "review-request",
    "Polite review request after a job",
    "owner / customer success / service provider",
    "happy customer, client",
    BASE + ["review_link"],
    [0, 5, 12],
    [
        (
            "First nudge",
            "How did we do on {{project_or_ref}}?",
            "Thank you for choosing us for {{project_or_ref}}. If you have two minutes, a short review would help us a lot: {{review_link}}\n\nIf anything wasn't right, reply to me directly and I'll fix it first.\n\nThanks,",
        ),
        (
            "Second reminder",
            "A quick favour about {{project_or_ref}}",
            "A gentle reminder in case my last note got buried. An honest review, even a sentence or two, helps other customers and helps us improve: {{review_link}}\n\nThank you,",
        ),
        (
            "Final notice",
            "Last note about your review",
            "This is my last note about this. If you'd like to share your experience of {{project_or_ref}}, the link is here: {{review_link}} No problem at all if not, and thank you again for your business.\n\nBest wishes,",
        ),
    ],
)

sc(
    "meeting-reschedule",
    "No-show or unanswered reschedule",
    "sales / customer success / scheduler",
    "prospect, client, partner",
    BASE,
    [0, 3, 7],
    [
        (
            "First nudge",
            "Let's find a new time for {{project_or_ref}}",
            "We missed each other for {{project_or_ref}} on {{due_date}}, no problem. Could you suggest two times that work for you over the next week? I'll confirm one right away.\n\nThanks,",
        ),
        (
            "Second reminder",
            "Still keen to meet about {{project_or_ref}}",
            "I'd still like to find a time for {{project_or_ref}}. If it's easier, reply with two windows that suit you and I'll fit in around them.\n\nThank you,",
        ),
        (
            "Final notice",
            "Should I close this out?",
            "I haven't been able to find a time for {{project_or_ref}}, so I'll close this on my side. If now isn't the right moment, reply \"later\" and I'll check back next month. If you'd like to meet, reply with a time that works.\n\nAll the best,",
        ),
    ],
)

os.makedirs(OUT_DIR, exist_ok=True)

for i, sc_ in enumerate(S):
    steps = sc_["steps"]
    out = [
        "---",
        f"slug: {sc_['slug']}",
        f"title: {sc_['title']}",
        f"who_sends: {sc_['who_sends']}",
        f"who_receives: {sc_['who_receives']}",
        f"fields: [{', '.join(sc_['fields'])}]",
        f"cadence_days: [{', '.join(map(str, sc_['cad']))}]",
        "---",
    ]
    for n, (name, subj, body) in enumerate(steps):
        out.append(f"## Step {n + 1}: {name} (day {sc_['cad'][n]})")
        out.append(f"Subject: {subj}")
        out.append("Body:")
        out.append("Hi {{recipient_first_name}},\n")
        body = body.rstrip()
        out.append(body)
        out.append(SIG + "\n")
    open(os.path.join(OUT_DIR, f"{i + 1:02d}-{sc_['slug']}.md"), "w").write("\n".join(out))

json.dump(
    {"allowed_fields": sorted({f for s in S for f in s["fields"]})},
    open(os.path.join(OUT_DIR, "_schema.json"), "w"),
    indent=2,
)
