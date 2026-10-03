import { execFileSync } from "node:child_process";
import { readFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { describe, expect, it } from "vitest";

const root = join(dirname(fileURLToPath(import.meta.url)), "..");

describe("pack build", () => {
  it("writes cover, index, 12 sections, legal line, and imprint", () => {
    execFileSync("python3", [join(root, "build/pack.py")], { cwd: root, stdio: "pipe" });
    const md = readFileSync(join(root, "dist/pack.md"), "utf8");
    const txt = readFileSync(join(root, "dist/pack.txt"), "utf8");
    for (const pack of [md, txt]) {
      expect(pack).toContain("Chase-email templates");
      expect(pack).toContain("12 scenarios, 3 steps each");
      expect(pack).toContain("How to use");
      expect(pack).toContain("Cadence");
      expect(pack).toContain("coi-chase");
      expect(pack).toContain("meeting-reschedule");
      expect(pack).toContain("Templates are general business correspondence, not legal advice.");
      expect(pack).toContain(
        "ZenStudy Technologies FZCO, Technohub 1, Dubai Silicon Oasis, Dubai, UAE",
      );
    }
  });
});
