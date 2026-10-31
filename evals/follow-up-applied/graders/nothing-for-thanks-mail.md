---
type: regex
target:
  source: file
  path: workspace-home/tasks.md
pattern: '- \[ \] [^\n]*(?:[Tt]hank|[Aa]rchitecture summary)'
match: not_contains
weight: 2
---
