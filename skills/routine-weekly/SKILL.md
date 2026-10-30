---
name: routine-weekly
description: Runs a short weekly review. Looks back at the week, checks follow-ups, prepares next week's calendar, and chooses next week's tasks within the free hours. Use when the user says "weekly review", "plan next week", "review my week" or runs /routine-weekly, or on the weekly review day of the profile.
license: Apache-2.0
---

# Weekly review

The weekly review closes the week and prepares the next one in about the `Weekly review` time of the profile. The user sees what got done, which follow-ups wait, which meetings of next week need a decision, and which items fit into next week. Run it on the `Weekly review` day of the profile, or on request on any day.

Start by reading the `workspace-commons` skill and `<home>/profile.md`. Then read `<home>/tasks.md` and `<home>/state/routine.md`.

## Hard rules

1. Never send an email or a chat message. Drafts come only from the `mail-reply` skill, and the user sends them.
2. Change calendar events and responses only through the `meeting-schedule` skill. Never decline, move or delete an event without the user's approval.
3. Change `<home>/tasks.md` only through the `task-list` skill.
4. Write only `<home>/state/routine.md` yourself.
5. End every session with the closing step, also after "stop".

Run the steps as in "Sessions" of the `workspace-commons` skill. When a skill that a step names is not installed, show the change, and the user makes it by hand. "This week" is the current week. "Next week" is the following week, unless the user names another week. When `last_weekly` is already in this week, say so and ask which step to run.

## Steps

1. **Look back.** List the items of `## Done` with a date in this week and the open items of `## This week`, in 3 to 5 lines. Ask one optional question: "What went well this week, and what do you want to change?" Keep the answer short. When it names an action, capture it with `## Capture` of the `task-list` skill. Then write `last_weekly: <today>` to `<home>/state/routine.md`. When that file is missing, create it with the header in the home reference of `workspace-commons`.

2. **Follow-ups.** Run the `mail-follow-up` skill. Without it, list the items of `<home>/tasks.md` with `waiting:` and a `since:` date older than `Nudge after` of the profile. For each, propose keep (default), a reminder draft through the `mail-reply` skill, or drop through `## Complete and drop` of the `task-list` skill.

3. **Next week's calendar.** Read the working days of next week with `list events`. Show only what needs a decision:
   - unanswered invitations and overlapping events;
   - events after `Day end`, on a public holiday, or on an absence day;
   - at most 3 recurring series: those that the user declined or left unanswered in the last 2 weeks, or those with no agenda;
   - days without a free slot of the `Focus block` length.

   A series with a decision in `## Decisions` of `<home>/state/routine.md` is not asked about again. Ask in one call, as separate questions:
   - The answers to invitations and the decisions on recurring series (keep or decline). An answer notifies the organizer, so this question has no recommended option. Propose the answers by `## Answer invitations` of the `meeting-schedule` skill.
   - The focus blocks, as a default batch, by `## Block focus time` of the `meeting-schedule` skill.
   - "Are you away on any day next week?" Take out-of-office events as absences too.

   The `meeting-schedule` skill applies the approved answers and blocks without asking again. When a decline needs a message, offer the `mail-reply` skill. Without a calendar tool, ask only for the absences and the total meeting hours of next week.

   Then write the absences to `## Absences` of `<home>/state/routine.md`. Write each decision on a recurring series to `## Decisions`, also "keep". Remove the absences that ended before the last working day, and the decisions about series that ended.

4. **Choose next week.** Take the free hours of each working day of next week, as `workspace-commons` defines them, with the busy time after step 3. A day never has less than 0 free hours.

   Propose `## This week` within the sum of free hours, most important first:
   1. items with `due:` in next week, from any section;
   2. open items of `## This week` that still matter (the others go back to `## Backlog`);
   3. the next items from the top of `## Backlog`.

   Skip items with `waiting:`. For a `larger` item, count only its next step. Propose a size for an item without `est:`. Add one line on what stays out on purpose, for example "Not next week, on purpose: X and Y." When the free hours are 0, propose an empty `## This week`. After the answer, set `## This week` with `## Plan week` of the `task-list` skill. Then run `## Groom` of the `task-list` skill, limited to the raw captures.

5. **Close the review.** Show one message with what changed: tasks, calendar answers, focus blocks, drafts, absences and decisions. Add the 3 most important items of next week, and the planned hours of `## This week` against the free hours of next week.
