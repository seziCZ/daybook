# Writing a daybook skill

Read these rules before you write or change a skill, together with the `workspace-commons` skill and its two reference files.

## Two principles

- **Simple.** A person must be able to read a skill once and trust it. The reader sees what the skill reads, what it may write, and when it asks first. Prefer removing or merging a rule over adding one, and use plain words with no hidden logic.
- **Practical.** Keep only skills that people really use. Drop or merge a skill that a busy professional with Google Workspace would not use at least weekly, or whose job another skill already does. Section 3 of [spec.md](spec.md) records these decisions.

## Shape

- One folder `skills/<name>/` with `SKILL.md`. Add `references/`, `assets/` or `scripts/` only when the skill needs them, and keep them one level deep.
- The name is `<family>-<object>` in kebab-case, the same as the folder. The families are `workspace-`, `routine-`, `task-`, `mail-`, `meeting-` and `write-`.
- The frontmatter has exactly three fields: `name`, `description` and `license: Apache-2.0`. Other fields break the Agent Skills specification.
- The description is in the third person. It says what the skill does, then "Use when ..." with the words that users say (inbox, calendar, meeting, todo). Keep it under 400 characters, with no angle brackets (`<` or `>`).
- Aim for 40 to 80 lines in `SKILL.md`, and never write more than 120. Every line costs context in every session that loads the skill.

## Body

1. `# Title`, then one paragraph on the purpose: what the user gets, and when.
2. One line: "Start by reading the `workspace-commons` skill and `<home>/profile.md`."
3. `## Hard rules`: numbered, only the things that must never go wrong. Repeat the one-line safety rules that matter for this skill, for example "Never send an email.", so that the skill stays safe when it is installed alone.
4. `## Steps`: numbered, each with a bold lead word, for example "1. **Read the calendar.** ...". A skill with several procedures has one section per procedure instead.
5. Reference sections, such as formats, tables and examples, follow the section that uses them.
6. A skill that runs a session follows "Sessions" in `workspace-commons` and ends with a closing step. Do not repeat the session format in the skill.

## Words

- Name a tool action by its capability in backticks, for example `search mail` or `list events`. Never name a connector tool or a `gws` command in a skill, because the capability map in `workspace-commons` does that.
- Name another skill as "the `task-list` skill", and a home file as `<home>/tasks.md`.
- Take every personal preference (hours, durations, names, senders, formats) from `<home>/profile.md`, by its key. A fixed rule of the procedure may name a number in the skill, for example "the last 14 days of mail". Add a profile key only when users will really want to change the value.
- Use forward slashes in paths.
- Use fictional examples: Alex, Maria, `example.com`.
- Write plain international English: short sentences of about 15 words, common words, no idioms, and no em dash or en dash. Write "2 to 4", not "2-4".
- Say what to do, not what to avoid, unless it is a hard rule.

## Writes

A skill writes only what the table "Who writes what" in `workspace-commons` allows. To change anything else, it calls the owner skill. Every write follows an approval: the skill shows the exact change as a default batch and writes after the answer. Hard rule 4 of `workspace-commons` lists the exceptions. Do not repeat a rule of `workspace-commons` in a skill, except the one-line safety rules.

## Checks

- `python -I -B scripts/lint.py` passes. It checks the frontmatter, the references to skills, sections, capabilities, profile keys and home files, the dashes, and the eval cases.
- `agentskills validate skills/<name>` passes (from the `skills-ref` package).
- The skill reads well when it is the only skill installed besides `workspace-commons`.
- The approval histories of the changed skills are recorded again, and the eval cases pass, as [evals/README.md](../evals/README.md) describes.
