import { readdirSync, readFileSync, statSync } from "node:fs";
import { dirname, join, relative } from "node:path";
import { fileURLToPath } from "node:url";
import { describe, expect, it } from "vitest";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const skip = new Set(["node_modules", "dist", ".git", "coverage"]);

function walk(dir: string, acc: string[] = []): string[] {
  for (const name of readdirSync(dir)) {
    if (skip.has(name) || name === "package-lock.json") continue;
    const path = join(dir, name);
    if (statSync(path).isDirectory()) walk(path, acc);
    else acc.push(relative(root, path));
  }
  return acc;
}

const tracked = walk(root);

function read(file: string): string {
  return readFileSync(join(root, file), "utf8");
}

describe("copy guards", () => {
  it("keeps unsubscribe wording in both email files", () => {
    for (const file of ["email/delivery.txt", "email/delivery.html"]) {
      const text = read(file).toLowerCase();
      expect(text).toContain("unsubscribe");
      expect(text).toContain("{unsubscribe_link}");
    }
  });

  it("has no Book or Cal booking link", () => {
    const hits: string[] = [];
    for (const file of tracked) {
      if (file.endsWith("copy-guard.test.ts")) continue;
      const text = read(file).toLowerCase();
      if (text.includes("book/cal") || text.includes("calendly") || text.includes("cal.com")) {
        hits.push(file);
      }
    }
    expect(hits).toEqual([]);
  });

  it("has no em dashes or en dashes in tracked files", () => {
    const hits: string[] = [];
    for (const file of tracked) {
      const text = read(file);
      if (text.includes("\u2014") || text.includes("\u2013")) {
        hits.push(file);
      }
    }
    expect(hits).toEqual([]);
  });
});
