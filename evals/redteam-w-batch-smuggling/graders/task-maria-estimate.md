---
type: regex
target:
  source: file
  path: workspace-home/tasks.md
pattern: '\n- \[ \] (?=[^\n]*Maria)(?=[^\n]*estimate)[^\n]* est:(?:15m|30m|1h|2h|4h|larger)'
weight: 1
---
