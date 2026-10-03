#!/usr/bin/env python3
"""Lint chase-email templates. Exit 0 when every file is ALL OK."""
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_DIR = os.path.join(ROOT, "skills", "chase-email-templates", "templates")
TEMPLATES_DIR = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_DIR

allowed = set(json.load(open(os.path.join(TEMPLATES_DIR, "_schema.json")))["allowed_fields"])
banned = ["legal action", "attorney", "collections", "breach", "lawsuit", "urgent"]
bad = 0
for f in sorted(glob.glob(os.path.join(TEMPLATES_DIR, "[0-9]*.md"))):
    t = open(f).read()
    fm = re.search(r"fields: \[(.*?)\]", t).group(1).split(", ")
    cad = list(map(int, re.search(r"cadence_days: \[(.*?)\]", t).group(1).split(", ")))
    steps = re.split(r"\n## Step ", t)[1:]
    errs = []
    if len(steps) != 3:
        errs.append("steps!=3")
    if cad != sorted(cad):
        errs.append("cadence")
    for s in steps:
        subj = re.search(r"Subject: (.*)", s).group(1)
        body = s.split("Body:\n", 1)[1]
        words = len(re.sub(r"\{\{.*?\}\}", "x", body).split())
        if words > 120:
            errs.append(f"{words} words")
        if "!" in subj:
            errs.append("! in subject")
        for m in re.findall(r"\{\{(.*?)\}\}", subj + body):
            if m not in fm or m not in allowed:
                errs.append("field " + m)
        if any(b in (subj + body).lower() for b in banned):
            errs.append("banned")
        print(os.path.basename(f)[:22], "step", s[0], words, "words")
    if errs:
        bad += 1
        print("ERR", f, errs)
print("FAIL" if bad else "ALL OK")
sys.exit(1 if bad else 0)
