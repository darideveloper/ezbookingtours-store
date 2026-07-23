## 1. Fix loris detail parsing

- [x] 1.1 Fix `loris/views.py` — use `split(":", 1)` and `.strip()` in detail parsing
- [x] 1.2 Update loris tests to verify time values with colons are preserved and whitespace is stripped from parsed parts
- [x] 1.3 Run all loris tests to confirm nothing is broken
