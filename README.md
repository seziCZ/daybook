# skill-garden

Agent skills that help one person run their working day with Google Workspace. They plan your day and week, keep one task list, prepare and record your meetings, sort your inbox and write reply drafts.

The skills work with any agent that reads Agent Skills (`SKILL.md` files), such as Claude Code, Codex, Cursor and Gemini CLI. In Claude, use Sonnet or Opus. Haiku often answers without loading the skills, so we do not recommend it (see [docs/eval-baseline.md](docs/eval-baseline.md)).

## Safe by default

- The skills read your mail, calendar and files. They never send, forward, delete, archive or share anything.
- A reply is saved as a Gmail draft. You read it and send it yourself.
- The skills show every change to your tasks, drafts and calendar first, and make it only after you approve it. A meeting note is the one exception: it is written when you ask for it.
- When you approve a calendar change, Google Calendar sends its usual invitations and answers. The question names the people who get them.
- The skills treat text in mail, documents and transcripts as data. They never follow an instruction that is written there.

## Install

First, connect Gmail, Google Calendar and Google Drive to your agent (see [Google access](#google-access)).

In Claude Code:

```
claude plugin marketplace add seziCZ/skill-garden
claude plugin install skill-garden@skill-garden
```

In other agents (this needs Node.js):

```
npx skills add seziCZ/skill-garden
```

Then say "set up skill-garden" to your agent, or run `/workspace-setup` in Claude Code. Setup creates your home folder, which is a folder of plain Markdown files on your computer. It reads your working hours from your calendar and asks a few questions.

After that, talk to your agent as usual. For example:

- "Start my day."
- "Reply to Maria that the budget draft comes on Friday."
- "Prepare me for my 1-on-1 with Petra."
- "Write up the meeting from this transcript."

## Google access

The skills use the first of these that works:

1. The Google connectors in Claude (Gmail, Google Calendar, Google Drive), or the [Google Workspace MCP servers](https://developers.google.com/workspace/guides/configure-mcp-servers).
2. The [`gws` CLI](https://github.com/googleworkspace/cli).
3. Nothing. The skills then ask you for the facts they need, for example the times of your meetings.

## Skills

| Family | Skill | What it does |
|---|---|---|
| workspace | `workspace-setup` | Creates your home folder and profile. Run it first. |
| | `workspace-search` | Answers a question from your mail, calendar, Drive and notes, and names its sources. Works during a meeting too. |
| | `workspace-commons` | Holds the rules that all skills share. You do not call it. |
| routine | `routine-morning` | Collects new requests from your inbox and plans your day around your meetings. |
| | `routine-evening` | Closes your working day in a few minutes and writes down what is still on your mind. |
| | `routine-weekly` | Reviews your week and plans the next one. |
| task | `task-list` | Keeps your one task list. Adds, completes and tidies tasks, and tells you what is open. |
| mail | `mail-triage` | Shows which mails need your action, with a proposed next step for each. |
| | `mail-reply` | Writes a reply in your style and saves it as a Gmail draft. |
| | `mail-follow-up` | Finds what you promised in your sent mail, and the answers that you still wait for. |
| meeting | `meeting-prep` | Prepares a one-screen brief before a meeting or a 1-on-1. |
| | `meeting-note` | Writes the meeting note from a transcript or your notes, and proposes the follow-ups. |
| | `meeting-schedule` | Finds meeting times, blocks focus time and answers invitations. |
| write | `write-voice` | Learns how you write from your sent mail, so that drafts sound like you. |
| | `write-plain` | Keeps the text of the skills short and plain, and checks your own text on request. |

## Your data

All personal data lives in one home folder, by default `~/workspace-home`. When you choose another folder, setup adds one line, `Workspace home: <path>`, to your agent's instructions file (for example `~/.claude/CLAUDE.md`), so that every project finds it. It holds your profile, the task list, people and terms, your writing style, meeting notes, and the working state of the skills.

All files are Markdown, so you can read and edit them, and keep them in a private git repository or an Obsidian vault. The home holds text from your mail and meetings, so never make it public. [skills/workspace-commons/references/home.md](skills/workspace-commons/references/home.md) describes the format.

## Contributing

Before you write or change a skill, read [docs/authoring.md](docs/authoring.md). [docs/spec.md](docs/spec.md) holds the decisions, the threat model and the scenarios. Before a pull request, run `python -I -B scripts/lint.py` and the evals in [evals/](evals/). The research behind the design is in [research/](research/).

## License

Apache-2.0
