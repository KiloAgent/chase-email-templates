#!/usr/bin/env python3
"""Build dist/pack.md and dist/pack.txt from the committed templates."""
import glob
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES_DIR = os.path.join(ROOT, "skills", "chase-email-templates", "templates")
OUT_DIR = os.path.join(ROOT, "dist")
LEGAL = "Templates are general business correspondence, not legal advice."
IMPRINT = "ZenStudy Technologies FZCO, Technohub 1, Dubai Silicon Oasis, Dubai, UAE"

COVER_MD = """# Chase-email templates

12 scenarios, 3 steps each

## How to use

Pick a scenario. Replace every {{field}} with the real value. Send Step 1 on day 0. If there is no reply, wait until the next cadence day and send that step. Read the message once before you send it.

## Cadence

Each scenario lists `cadence_days`. Those numbers are days after the first send. Step 1 is day 0.
"""

COVER_TXT = """Chase-email templates

12 scenarios, 3 steps each

How to use

Pick a scenario. Replace every {{field}} with the real value. Send Step 1 on day 0. If there is no reply, wait until the next cadence day and send that step. Read the message once before you send it.

Cadence

Each scenario lists cadence_days. Those numbers are days after the first send. Step 1 is day 0.
"""


def parse(path):
    text = open(path).read()
    slug = re.search(r"^slug: (.*)$", text, re.M).group(1).strip()
    title = re.search(r"^title: (.*)$", text, re.M).group(1).strip()
    who_sends = re.search(r"^who_sends: (.*)$", text, re.M).group(1).strip()
    who_receives = re.search(r"^who_receives: (.*)$", text, re.M).group(1).strip()
    fields = re.search(r"^fields: \[(.*)\]$", text, re.M).group(1)
    cad = re.search(r"^cadence_days: \[(.*)\]$", text, re.M).group(1)
    body = text.split("---", 2)[2].strip()
    return {
        "file": os.path.basename(path),
        "slug": slug,
        "title": title,
        "who_sends": who_sends,
        "who_receives": who_receives,
        "fields": fields,
        "cad": cad,
        "body": body,
    }


def main():
    items = [parse(path) for path in sorted(glob.glob(os.path.join(TEMPLATES_DIR, "[0-9]*.md")))]
    if len(items) != 12:
        raise SystemExit(f"expected 12 templates, found {len(items)}")

    md = [COVER_MD.rstrip(), "", "## Index", ""]
    txt = [COVER_TXT.rstrip(), "", "Index", ""]
    for i, item in enumerate(items, 1):
        md.append(f"{i}. [{item['title']}](#{item['slug']}) (`{item['slug']}`)")
        txt.append(f"{i}. {item['title']} ({item['slug']})")
    md.append("")
    txt.append("")

    for item in items:
        md.extend(
            [
                f"## {item['title']}",
                "",
                f"slug: {item['slug']}",
                f"who_sends: {item['who_sends']}",
                f"who_receives: {item['who_receives']}",
                f"fields: [{item['fields']}]",
                f"cadence_days: [{item['cad']}]",
                "",
                item["body"],
                "",
            ]
        )
        txt.extend(
            [
                item["title"],
                "",
                f"slug: {item['slug']}",
                f"who_sends: {item['who_sends']}",
                f"who_receives: {item['who_receives']}",
                f"fields: [{item['fields']}]",
                f"cadence_days: [{item['cad']}]",
                "",
                item["body"],
                "",
            ]
        )

    md.extend(["## Back", "", LEGAL, "", IMPRINT, ""])
    txt.extend(["Back", "", LEGAL, "", IMPRINT, ""])

    os.makedirs(OUT_DIR, exist_ok=True)
    open(os.path.join(OUT_DIR, "pack.md"), "w").write("\n".join(md).rstrip() + "\n")
    open(os.path.join(OUT_DIR, "pack.txt"), "w").write("\n".join(txt).rstrip() + "\n")
    print("wrote dist/pack.md and dist/pack.txt")


if __name__ == "__main__":
    main()
