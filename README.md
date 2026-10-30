# skill-garden

Agent skills that help one person run their working day with Google Workspace: a morning and an evening routine, a weekly review, one task list, meeting preparation and notes, mail triage and reply drafts.

The skills work with any agent that reads Agent Skills (`SKILL.md`), such as Claude Code, Codex, Cursor and Gemini CLI.

## Safe by default

- The skills read your mail, calendar and files. They never send, forward, delete, archive or share mail or files.
- A reply is written as a Gmail draft. You read it and send it yourself.
- Every change to your tasks, drafts and calendar is shown first and applied only after you approve it. When you approve a calendar change, Google Calendar sends its usual invitations and answers, and the question names who gets them.
- A meeting note is written when you ask for it.
- Text in mail and documents is treated as data. An instruction inside an email is never followed.

## Install

Claude Code:

```
claude plugin marketplace add <owner>/skill-garden
claude plugin install skill-garden@skill-garden
```

Other agents:

```
npx skills add <owner>/skill-garden
```

Then run the `workspace-setup` skill. It creates your home folder, learns your working hours from your calendar, and asks a few questions.

## Google access

The skills use the first of these that works:

1. The Google connectors in Claude (Gmail, Google Calendar, Google Drive), or the [Google Workspace MCP servers](https://developers.google.com/workspace/guides/configure-mcp-servers).
2. The [`gws` CLI](https://github.com/googleworkspace/cli).
3. Nothing: the skills ask you for the facts they need, for example the hours of your meetings.

## Skills

| Family | Skill | What it does |
|---|---|---|
| workspace | `workspace-setup` | Creates your home folder and profile. Run it first. |
| | `workspace-search` | Answers one question with its sources from mail, calendar, Drive and your notes. |
| | `workspace-commons` | Shared rules of all skills. You do not call it directly. |
| routine | `routine-morning` | Inbox hints, capture, and the plan of the day around your meetings. |
| | `routine-evening` | Closes the working day in a few minutes, so that work stays at work. |
| | `routine-weekly` | Reviews the week and plans the next one. |
| task | `task-list` | Keeps your one task list: capture, complete, groom, query. |
| mail | `mail-triage` | Shows which threads need your action, with a proposed outcome. |
| | `mail-reply` | Drafts a reply in your voice into Gmail drafts. |
| | `mail-follow-up` | Finds your promises and the answers you still wait for. |
| meeting | `meeting-prep` | A one-screen brief before a meeting or a 1-on-1. |
| | `meeting-note` | Writes the meeting note from a transcript or your notes, and proposes follow-ups. |
| | `meeting-assist` | Short answers during a meeting, and remarks stored for the note. |
| | `meeting-schedule` | Finds a time, protects focus time, answers invitations. |
| write | `write-voice` | Learns how you write from your sent mail, and writes like you. |
| | `write-plain` | Plain international English for the text that these skills write, and a check of your own text. |

## Your data

All personal data lives in one home folder (default `~/workspace-home`): your profile, the task list, people and terms, your voice, meeting notes, and the working state of the skills. All files are Markdown, so you can read and edit them, and keep them in a private git repository or an Obsidian vault. The home holds text from your mail and meetings, so never make it public. The format is in [skills/workspace-commons/references/home.md](skills/workspace-commons/references/home.md).

## Contributing

Read [docs/authoring.md](docs/authoring.md) before you write or change a skill, and [docs/spec.md](docs/spec.md) for the decisions, the threat model and the scenarios. Before a pull request, run `python -I -B scripts/lint.py` and the evals in [evals/](evals/). The research behind the design is in [research/](research/).

## License

Apache-2.0
