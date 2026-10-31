---
name: task-list
description: Keeps the user's one task list in the home folder. Captures tasks with a size, completes and drops them, plans the day and the week, closes the day and grooms the list. Answers questions about open work. Use when the user adds, ticks or drops a task, says remind me to, asks what is open, what is on their plate today or this week or what they wait on, or when another skill changes tasks.md.
license: Apache-2.0
---

# Task list

This skill keeps one task list, `<home>/tasks.md`, and is the only skill that writes it. The user gets a short list in priority order where every task has a size. Use it directly to add, finish or find tasks. Other skills call its sections by name.

Start by reading the `workspace-commons` skill and `<home>/profile.md`.

## Hard rules

1. Show the proposed changes as a default batch, and write them after the answer. When a calling skill passes changes that the user approved, write them without asking again.
2. Never delete an item. A finished item moves to Done with `done:`, an unneeded one with `dropped:`.
3. Every item except a raw capture has a size. Propose the size, and never ask for it.
4. Change This week, reorder the Backlog, or fill Today only after the user confirms it.
5. Write only `<home>/tasks.md`. Never send an email or change the calendar.

The file and item format is the `tasks.md` section of the home reference in the `workspace-commons` skill. When `<home>/tasks.md` is missing, create it with the four empty sections of that format at the first write.

## Capture

1. **Give one outcome.** Each request gets one outcome: task, waiting on someone, or not captured (say why in a few words). Outside a routine, a request can also be "do now": a few minutes, done in this session, with no item. A routine only captures.
2. **Write the item.** Start the action with a verb and name the result. Add a tag from `Task tags` of the profile when one fits. Propose the size from the text. Add `due:` only when the user or the source names a date. A waiting item gets `waiting:<Name> since:<the date the caller passes, otherwise today>`. When a note in the `Meeting notes folder` of the profile matches by keyword, add a link to it.
3. **Skip duplicates.** A duplicate is defined in the `tasks.md` section of the home reference. Say so, and skip it.
4. **Place it.** Put the item into the Backlog by priority. Propose This week when the work is needed this week, which includes every item that is due this week or already overdue. When the item comes from a raw capture, replace that raw line.
5. **Raw capture.** When a calling skill passes a line in the user's own words, write `- [ ] <the user's words>` at the top of the Backlog. Skip steps 1 to 4. `## Groom` turns it into an item later.

```
- [ ] call the bank about the new card
- [ ] (Hiring) Send the interview plan to Maria est:30m due:2026-11-04
- [ ] (Work) Ready the Q3 budget review est:larger
  - [ ] Draft the cost table est:2h
- [ ] (Work) Get the signed contract est:15m waiting:Alex since:2026-10-20
```

## Complete and drop

1. **Complete.** Move a finished item to the top of Done with `done:YYYY-MM-DD`, the day the work was done. Its sub-items move with it.
2. **Drop.** Move an item that is no longer needed to Done with `dropped:YYYY-MM-DD (<reason>)`.
3. **Next step.** A finished next step stays under its parent as `- [x] <step> est:<size> done:YYYY-MM-DD`. Propose the next step of 1 to 2 hours for the parent, or propose to complete the parent.

## Plan today

The `routine-morning` skill passes a plan that the user has already approved, so do not ask again.

1. **Check.** When Today holds a plan with an earlier date, stop and tell the calling skill to close that day first.
2. **First line.** Write `Plan YYYY-MM-DD: end HH:MM, free HH:MM to HH:MM, HH:MM to HH:MM.` with today's date and the times of the plan.
3. **Items.** Move each planned item from This week or the Backlog into Today, in the order of the plan. Write `- [ ] HH:MM <item>` where a time matters, otherwise `- [ ] <item>`. For a `larger` item, move only its next step, and add `(step of: <parent action>)` to it.

## Plan week

The `routine-weekly` skill passes the plan of the next week, which the user has already approved, so do not ask again.

1. **Replace.** Write the planned items into This week, in the priority order of the plan. Move each one from This week or the Backlog, so that no item appears twice.
2. **Carry over.** Keep unfinished items of the old This week that the plan names, with their priority. Return the others to the top of the Backlog in their old order.

## End of day

A calling skill runs this when it closes a day. The caller is the `routine-evening` skill in its step **Tick the day**, or the `routine-morning` skill as a fallback. The closed day is the date on the `Plan` line, unless the caller passes a day.

1. **Done.** Move the checked items, and the items that the caller names as finished, to Done with the date of the closed day. Finished work that matches an open item completes it. Other finished work is not recorded. A finished next step goes back under its parent, as in `## Complete and drop` step 3.
2. **Unfinished.** Return the unchecked items, without their times, to the top of This week in their Today order. A next step returns under its parent, without `(step of: ...)`.
3. **Other lines.** Every other line that the user wrote in Today goes to the top of the Backlog as a raw capture.
4. **Empty.** Empty Today, including its `Plan` line.

## Groom

1. **Close checked items.** Move checked items outside Today to Done, with today's date when they have no `done:` date. A checked next step under an open parent stays there.
2. **Normalize.** Fix the format: a verb first, a tag from the profile, the fields in order. Propose a size for each item without one. Turn raw captures into items through `## Capture`, and ask about a line that you cannot read as a task. With many changes, propose them in batches of about 15.
3. **Flag waiting.** List the `waiting:` items with a `since:` date older than `Nudge after` of the profile. Offer a reminder mail with the `mail-reply` skill.
4. **Report.** Give the counts per section, the flagged waiting items, the items still without a size, and anything unclear.

A caller may limit Groom to the raw captures. Then run only step 2 (**Normalize**) for the raw captures.

## Query

Answer with a short list filtered by tag, `waiting:`, `due:` or size. For example: "what is open on Hiring", "what am I waiting on from Maria", "what is due this week" or "what takes 15m". Show the section of each item. A query never changes the file.

## Finish

After each write, say in one line what changed, for example "Added 2 tasks to the Backlog and moved 1 to Done."
