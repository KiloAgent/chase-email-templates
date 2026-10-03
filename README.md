# chase-email-templates

Twelve follow-up scenarios, three steps each: first nudge, second reminder, final notice. Plain text with `{{field}}` merge tokens.

Hosted tool: [https://www.kiloagent.com/tools/chase-emails](https://www.kiloagent.com/tools/chase-emails)

The agent skill is `skills/chase-email-templates/` ([agentskills.io](https://agentskills.io/specification), [skills CLI](https://www.npmjs.com/package/skills)). That folder is self-contained. The templates live in `skills/chase-email-templates/templates/` so they copy with the skill.

## Install

Copy `skills/chase-email-templates/` into one of:

- `.claude/skills/chase-email-templates/`
- `.cursor/skills/chase-email-templates/`
- `.codex/skills/chase-email-templates/`
- `.github/skills/chase-email-templates/`

Verified with `skills@latest` from a clean temp directory against `main`. Cursor project install lands in `.agents/skills/`. Claude Code lands in `.claude/skills/`.

```bash
npx --yes skills@latest add KiloAgent/chase-email-templates --list -y
npx --yes skills@latest add KiloAgent/chase-email-templates --copy -y -a cursor -s chase-email-templates
npx --yes skills@latest add KiloAgent/chase-email-templates --copy -y -a claude-code -s chase-email-templates
```

From a local clone:

```bash
npx skills add . --list -y
npx skills add . --copy -y -a cursor -s chase-email-templates
```

Chat users with no skills directory: paste `PASTE_IN.md` into the chat.

## How an agent uses this

1. Pick a scenario file under `skills/chase-email-templates/templates/`.
2. Fill the front-matter fields. `build/merge.js` does this in the browser or in Node with no dependencies.
3. Choose the step from `cadence_days` and days since the first send.
4. Send through the user's own email tool only after the user approves that send. Never send automatically.

## Merge

Client-side only. Field values stay in the page until a visitor submits the email gate on the hosted tool.

```js
import { merge } from "./build/merge.js";

const text = merge("Hi {{recipient_first_name}},", { recipient_first_name: "Alex" });
```

Unknown fields and unclosed braces throw. After a successful fill there should be no leftover `{` or `}`.

## Templates

`build/gen.py` is the source of the 12 files and `templates/_schema.json`. The committed copies live next to `SKILL.md` so an install includes them.

```text
skills/chase-email-templates/templates/01-coi-chase.md
skills/chase-email-templates/templates/02-invoice-overdue.md
skills/chase-email-templates/templates/03-missing-document.md
skills/chase-email-templates/templates/04-contract-signature.md
skills/chase-email-templates/templates/05-quote-followup.md
skills/chase-email-templates/templates/06-appointment-confirmation.md
skills/chase-email-templates/templates/07-portal-access.md
skills/chase-email-templates/templates/08-approval-request.md
skills/chase-email-templates/templates/09-onboarding-info.md
skills/chase-email-templates/templates/10-delivery-status.md
skills/chase-email-templates/templates/11-review-request.md
skills/chase-email-templates/templates/12-meeting-reschedule.md
skills/chase-email-templates/templates/_schema.json
```

Each file has YAML front matter (`slug`, `title`, `who_sends`, `who_receives`, `fields`, `cadence_days`) and three steps with a Subject and a Body.

## Evals

Lint rules in `skills/chase-email-templates/evals/`. No network and no API keys.

```bash
npm test
npm run evals
```

Checks: three steps, Subject and Body, body at most 120 words, fields listed in front matter and `_schema.json`, banned phrases, ascending cadence, and a sample fill with no leftover braces.

## Scripts

```bash
npm install
npm run generate
npm run lint
npm run typecheck
npm test
npm run build
```

Node 20 or newer. `npm run generate` writes the template files from `build/gen.py`. `npm run lint` must print `ALL OK`. `npm run build` writes `dist/pack.md` and `dist/pack.txt` (cover, index, one section per scenario, the legal back line, and the imprint). Those pack files are build output and are not committed.

Landing copy lives in `landing/`. Delivery email copy lives in `email/`.

## Contributing

Open an issue or a PR against `main`. Run `npm test` and `npm run build` before you push. Keep copy free of em dashes, en dashes, and sales CTAs. License is MIT.
