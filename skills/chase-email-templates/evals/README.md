# Chase-email evals

Lint of the 12 template files. No network and no API keys. Run from the repository root.

| Check | Intent |
| --- | --- |
| files | 12 files named `01-coi-chase.md` through `12-meeting-reschedule.md` plus `_schema.json` |
| steps | each file has exactly 3 steps |
| subject_body | each step has Subject and Body |
| words | each body is at most 120 words |
| fields | every `{{field}}` is in that file's front matter and in `_schema.json` |
| banned | no legal action, attorney, collections, breach, lawsuit, or urgent |
| cadence | `cadence_days` is ascending |
| render | sample fields fill with no leftover braces |
| gen | committed templates match `build/gen.py` |

```bash
npm test
npm run evals
```
