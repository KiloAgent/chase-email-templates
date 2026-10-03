import { describe, expect, it } from "vitest";
import { hasLeftoverBraces, merge } from "../build/merge.js";

describe("merge", () => {
  it("replaces {{field}} tokens", () => {
    expect(merge("Hi {{recipient_first_name}},", { recipient_first_name: "Alex" })).toBe(
      "Hi Alex,",
    );
  });

  it("throws on an unknown field", () => {
    expect(() => merge("Hi {{other}},", { recipient_first_name: "Alex" })).toThrow(
      "unknown field other",
    );
  });

  it("throws on an unclosed brace", () => {
    expect(() => merge("Hi {{recipient_first_name", { recipient_first_name: "Alex" })).toThrow(
      "unclosed brace",
    );
  });

  it("flags leftover braces after a fill", () => {
    expect(hasLeftoverBraces("Hi Alex,")).toBe(false);
    expect(hasLeftoverBraces("Hi {{recipient_first_name}},")).toBe(true);
  });
});
