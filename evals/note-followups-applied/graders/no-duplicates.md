---
type: regex
target:
  source: file
  path: workspace-home/tasks.md
pattern: '(Draft the Q3 budget estimate for Maria|tooling license costs|budget deadline|estimate to Maria)[\s\S]*\1'
match: not_contains
weight: 2
---
