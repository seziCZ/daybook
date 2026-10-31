# Changelog

## 0.1.0

The first release.

- 15 skills in six families: `workspace` (setup, search, commons), `routine` (morning, evening, weekly), `task` (task list), `mail` (triage, reply, follow-up), `meeting` (prep, note, schedule) and `write` (voice, plain).
- Safe by default. The skills never send mail. A reply is a Gmail draft that the user sends. Every change to tasks, drafts and the calendar is shown first and applied after approval. An invitation, an answer or a changed email address always gets its own question.
- All personal data in one home folder of Markdown files, outside the repository.
- Works with the Google connectors in Claude, the Google Workspace MCP servers, the `gws` CLI, or without a tool.
- 79 eval cases with mocked Gmail, Calendar and Drive, including 15 red-team cases. Scores per model are in [docs/eval-baseline.md](docs/eval-baseline.md). Use Sonnet or Opus. Haiku often skips loading the skills, so we do not recommend it.
