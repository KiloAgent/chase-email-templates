import { defineConfig } from "vitest/config";

export default defineConfig({
  test: {
    include: ["tests/**/*.test.ts", "skills/chase-email-templates/evals/**/*.test.ts"],
    environment: "node",
  },
});
