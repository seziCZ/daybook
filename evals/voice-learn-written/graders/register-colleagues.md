---
type: regex
target:
  source: file
  path: workspace-home/voice.md
pattern: '## [^\n]*(Internal|[Cc]olleague)[^\n]*\n[\s\S]*?Greeting:[^\n]*Hi <name>,[\s\S]*?Sign-off:[^\n]*Thanks, Alex[\s\S]*?Samples:'
weight: 2
---
