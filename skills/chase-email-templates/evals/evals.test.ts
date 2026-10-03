import { execFileSync } from "node:child_process";
import { mkdtempSync, readdirSync, readFileSync, rmSync } from "node:fs";
import { tmpdir } from "node:os";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { describe, expect, it } from "vitest";
import { hasLeftoverBraces, merge } from "../scripts/merge.js";
import {
  SAMPLE_FIELDS,
  EXPECTED_FILES,
  bannedHits,
  bodyWordCount,
  loadTemplate,
  usedFields,
  type Template,
} from "./parse.js";

const skillDir = dirname(fileURLToPath(new URL("../SKILL.md", import.meta.url)));
const templatesDir = join(skillDir, "templates");
const repoRoot = join(skillDir, "..", "..");
const schema = JSON.parse(readFileSync(join(templatesDir, "_schema.json"), "utf8")) as {
  allowed_fields: string[];
};
const allowed = new Set(schema.allowed_fields);

function loadAll(): Template[] {
  return EXPECTED_FILES.map((file) => loadTemplate(join(templatesDir, file), file));
}

describe("chase-email template lint", () => {
  it("has the 12 named files and a schema", () => {
    const names = readdirSync(templatesDir).sort();
    expect(names).toEqual([...EXPECTED_FILES, "_schema.json"].sort());
  });

  it("keeps committed templates in sync with gen.py", () => {
    const scratch = mkdtempSync(join(tmpdir(), "chase-gen-"));
    try {
      execFileSync("python3", [join(repoRoot, "build/gen.py"), scratch], { stdio: "pipe" });
      for (const file of [...EXPECTED_FILES, "_schema.json"]) {
        expect(readFileSync(join(scratch, file), "utf8")).toBe(
          readFileSync(join(templatesDir, file), "utf8"),
        );
      }
    } finally {
      rmSync(scratch, { recursive: true, force: true });
    }
  });

  for (const item of loadAll()) {
    describe(item.file, () => {
      it("has exactly 3 steps with Subject and Body", () => {
        expect(item.steps).toHaveLength(3);
        for (const step of item.steps) {
          expect(step.subject.length).toBeGreaterThan(0);
          expect(step.body.startsWith("Hi ")).toBe(true);
          expect(step.subject.includes("!")).toBe(false);
        }
      });

      it("keeps each body at or under 120 words", () => {
        for (const step of item.steps) {
          expect(bodyWordCount(step.body)).toBeLessThanOrEqual(120);
        }
      });

      it("lists every used field in front matter and _schema.json", () => {
        expect(item.fields.length).toBeGreaterThan(0);
        for (const field of item.fields) {
          expect(allowed.has(field)).toBe(true);
        }
        for (const step of item.steps) {
          for (const field of usedFields(step.subject, step.body)) {
            expect(item.fields).toContain(field);
            expect(allowed.has(field)).toBe(true);
          }
        }
      });

      it("uses an ascending cadence that matches the step days", () => {
        expect(item.cadence_days).toEqual([...item.cadence_days].sort((a, b) => a - b));
        expect(item.cadence_days).toHaveLength(3);
        expect(item.steps.map((step) => step.day)).toEqual(item.cadence_days);
      });

      it("avoids banned phrases", () => {
        for (const step of item.steps) {
          expect(bannedHits(step.subject, step.body)).toEqual([]);
        }
      });

      it("renders sample fields with no leftover braces", () => {
        const values = Object.fromEntries(item.fields.map((field) => [field, SAMPLE_FIELDS[field]]));
        for (const step of item.steps) {
          const subject = merge(step.subject, values);
          const body = merge(step.body, values);
          expect(hasLeftoverBraces(subject)).toBe(false);
          expect(hasLeftoverBraces(body)).toBe(false);
        }
      });
    });
  }
});
