---
type: regex
target:
  source: file
  path: workspace-home/tasks.md
pattern: '- \[ \] look into the flaky CI job\s*\n'
match: not_contains
weight: 2
---
