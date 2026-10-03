import { readFileSync } from "node:fs";

export type Step = {
  heading: string;
  day: number;
  subject: string;
  body: string;
};

export type Template = {
  file: string;
  slug: string;
  title: string;
  who_sends: string;
  who_receives: string;
  fields: string[];
  cadence_days: number[];
  steps: Step[];
  raw: string;
};

const BANNED = ["legal action", "attorney", "collections", "breach", "lawsuit", "urgent"];

export const SAMPLE_FIELDS: Record<string, string> = {
  recipient_first_name: "Alex",
  sender_name: "Jordan Lee",
  sender_company: "Northwind Ops",
  document_name: "W-9 form",
  due_date: "12 May 2026",
  project_or_ref: "Site B / PO-1042",
  review_link: "https://reviews.example.test/northwind",
};

export const EXPECTED_FILES = [
  "01-coi-chase.md",
  "02-invoice-overdue.md",
  "03-missing-document.md",
  "04-contract-signature.md",
  "05-quote-followup.md",
  "06-appointment-confirmation.md",
  "07-portal-access.md",
  "08-approval-request.md",
  "09-onboarding-info.md",
  "10-delivery-status.md",
  "11-review-request.md",
  "12-meeting-reschedule.md",
] as const;

export function parseTemplate(file: string, raw: string): Template {
  const slug = matchLine(raw, /^slug: (.*)$/m);
  const title = matchLine(raw, /^title: (.*)$/m);
  const who_sends = matchLine(raw, /^who_sends: (.*)$/m);
  const who_receives = matchLine(raw, /^who_receives: (.*)$/m);
  const fieldsLine = matchLine(raw, /^fields: \[(.*)\]$/m);
  const cadenceLine = matchLine(raw, /^cadence_days: \[(.*)\]$/m);
  const fields = fieldsLine.split(", ").filter(Boolean);
  const cadence_days = cadenceLine.split(", ").filter(Boolean).map((n) => Number(n));
  const chunks = raw.split(/\n## Step /).slice(1);
  const steps = chunks.map((chunk) => {
    const headingMatch = chunk.match(/^(\d+): (.*) \(day (\d+)\)/);
    if (!headingMatch) {
      throw new Error(`bad step heading in ${file}`);
    }
    const subjectMatch = chunk.match(/^Subject: (.*)$/m);
    if (!subjectMatch) {
      throw new Error(`missing Subject in ${file}`);
    }
    const bodyParts = chunk.split("Body:\n");
    if (bodyParts.length < 2) {
      throw new Error(`missing Body in ${file}`);
    }
    return {
      heading: headingMatch[2] ?? "",
      day: Number(headingMatch[3]),
      subject: subjectMatch[1] ?? "",
      body: bodyParts[1] ?? "",
    };
  });
  return {
    file,
    slug,
    title,
    who_sends,
    who_receives,
    fields,
    cadence_days,
    steps,
    raw,
  };
}

export function loadTemplate(path: string, file: string): Template {
  return parseTemplate(file, readFileSync(path, "utf8"));
}

export function bodyWordCount(body: string): number {
  return body.replace(/\{\{.*?\}\}/g, "x").split(/\s+/).filter(Boolean).length;
}

export function usedFields(subject: string, body: string): string[] {
  const found = new Set<string>();
  const text = subject + body;
  for (const match of text.matchAll(/\{\{(.*?)\}\}/g)) {
    if (match[1]) found.add(match[1]);
  }
  return [...found];
}

export function bannedHits(subject: string, body: string): string[] {
  const text = `${subject}\n${body}`.toLowerCase();
  return BANNED.filter((word) => text.includes(word));
}

function matchLine(raw: string, pattern: RegExp): string {
  const match = raw.match(pattern);
  if (!match?.[1]) {
    throw new Error(`missing ${pattern}`);
  }
  return match[1];
}
