# Home folder

The home holds all personal data of the user. The `workspace-setup` skill creates it from the templates in its `assets/home/` folder. All files are Markdown, so that the user can read them in any editor and git shows every change.

```
<home>/
  profile.md        who the user is and how they work
  tasks.md          the task list
  people.md         people and terms
  voice.md          how the user writes
  notes/meetings/   meeting notes
  state/            working data of the skills
```

## profile.md

Written by `workspace-setup`, and edited by the user. Each setting is one `Key: value` line under its heading. A skill reads the value by its key. When a key is missing or empty, the skill uses the default below and does not ask.

| Heading | Key | Example | Default |
|---|---|---|---|
| Me | `Name` | Alex Novak | none |
| Me | `Role` | Senior software engineer | none |
| Me | `Email` | alex@example.com | the address of the connected mail account |
| Me | `Time zone` | Europe/Prague | the time zone of the shell |
| Me | `Languages` | English, Czech | English |
| Me | `Note language` | English | English |
| Working time | `Working days` | Monday to Friday | Monday to Friday |
| Working time | `Day start` | 09:00 | 09:00 |
| Working time | `Day end` | 17:00 | 17:00 |
| Working time | `Planned hours` | 7 | 7 |
| Working time | `Focus block` | 90m | 90m |
| Working time | `Morning routine` | 20m | 20m |
| Working time | `Evening routine` | 10m | 10m |
| Working time | `Weekly review` | Friday 30m | Friday 30m |
| Mail | `Inbox query` | in:inbox category:primary | in:inbox |
| Mail | `Important senders` | maria@example.com, Finance team | none |
| Mail | `Hint limit` | 10 | 10 |
| Sources | `Sources I check by hand` | Slack, Jira | none |
| Tasks | `Task tags` | Work, Platform, Hiring | none (no tags) |
| Tasks | `Nudge after` | 7d | 7d |
| Notes | `Meeting notes` | markdown | markdown (or `google-doc`) |
| Notes | `Meeting notes folder` | notes/meetings | notes/meetings |

Durations are written as `30m`, `90m` or `7d`. `Weekly review` is a day and a duration. `Nudge after` is the age of a `waiting:` item after which the skills propose a reminder. `Meeting notes folder` is relative to the home.

Public holidays follow under the heading `## Public holidays`, one per line: `YYYY-MM-DD Name`.

## tasks.md

Written only by the `task-list` skill. Four sections, in this order:

- `## Today`: the plan of the current day. The first line is `Plan YYYY-MM-DD: end HH:MM, free HH:MM to HH:MM, HH:MM to HH:MM.`, with the date of the planned day. The items follow, with a start time where it matters: `- [ ] HH:MM <item>`.
- `## This week`: the items chosen for this week, by priority, top first.
- `## Backlog`: everything else, by priority, top first. Ideas without a commitment are at the bottom.
- `## Done`: finished and dropped items, newest first.

An item is one line:

```
- [ ] (<Tag>) <action> est:<size> due:YYYY-MM-DD waiting:<Name> since:YYYY-MM-DD <link>
```

- **Action:** starts with a verb and names the result, for example "Send the Q3 budget draft to Maria".
- **Tag:** optional, one of `Task tags` in the profile. Without tags in the profile, items have no tag.
- **Size:** `15m`, `30m`, `1h`, `2h`, `4h` or `larger`. A `larger` item carries its next step of 1 to 2 hours as a sub-item, and only the step is planned.
- **due:, waiting: and since:** only when real. `waiting:` names the person who owes something, and `since:` is the day it was asked.
- **Link:** optional, a Markdown link to a note or a web link.
- **Sub-item:** indented by two spaces, carries only `est:`. A finished sub-item stays checked under its open parent.
- **Next step in Today:** a sub-item planned for today appears in Today with `(step of: <parent action>)` at the end, so that `## End of day` of the `task-list` skill can return it under its parent.
- **Raw capture:** `- [ ] <the user's words>` without `est:`, at the top of the Backlog. The `task-list` skill turns it into an item later and replaces the line.
- **Duplicate:** two items with the same action for the same person or tag, when the other one is open or was done in the last 30 days.
- **Done:** `- [x] <item> done:YYYY-MM-DD`, or `dropped:YYYY-MM-DD (<reason>)` for an item that is no longer needed. Items are never deleted.

## people.md

Any skill may add a row, or correct a name, a role or a note, after the user approves it. An Email is added or changed only from the user's own words or from a header of mail that the user sent, in its own question with the old and the new address. No skill deletes a row.

```
# People and terms

## People

| Name | Who they are | Email | Notes |
|---|---|---|---|
| Maria Lopez | Finance lead, owns the budget | maria@example.com | Prefers short mails |

## Terms

| Term | Meaning |
|---|---|
| Q3 plan | The budget and hiring plan for July to September |
```

## voice.md

Written by the `write-voice` skill. It holds the user's greetings, sign-offs, tone and 3 to 6 sample sentences per language and audience. The `write-voice` skill defines the format. A `voice.md` without a register (a `## ` heading) counts as missing.

## Meeting notes

Written by the `meeting-note` skill into the `Meeting notes folder` of the profile. One note per meeting, named `YYYY-MM-DD <Topic> (<Person>).md`. Person is the first name of the main counterpart as in `people.md`, or two first names joined by " and ". With `Meeting notes: google-doc` in the profile, the note is a Google Doc with the same name, and the home keeps a Markdown file of the same name with one line: `[<name>](<doc url>)`.

## state/

Working data of the skills, kept between sessions. Only the skills on the `Written by:` line write a file, each right after the step that changes it, and without asking. The first skill that needs a missing file creates it with the header below. A scalar is a `key: value` line. A dated list has one entry per line, starting with `YYYY-MM-DD`.

`state/routine.md`:

```
# Routine state

Written by: routine-morning (last_morning), routine-evening (last_evening), routine-weekly (last_weekly, Absences, Decisions).

last_morning: YYYY-MM-DD
last_evening: YYYY-MM-DD
last_weekly: YYYY-MM-DD

## Absences

YYYY-MM-DD to YYYY-MM-DD <reason>

## Decisions

YYYY-MM-DD <recurring meeting>: <decision>
```

`state/meeting-assist.md`:

```
# Meeting assist state

Written by: meeting-assist appends remarks; meeting-note removes the lines it used and the old lines that the user drops.

YYYY-MM-DD HH:MM | <meeting> | <remark>
```

`state/mail-follow-up.md`:

```
# Mail follow-up state

Written by: mail-follow-up (last_scan).

last_scan: YYYY-MM-DD
```
