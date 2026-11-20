# P05 – Object Inspector (Mutability Detective)

**Team size:** 2  **Builds on:** all of Day 3 – Lessons 01–07, Deep Dive 03 (grid trap) and Deep Dive 04 (hashability)

## Problem statement
Build a teaching tool for your juniors that **proves** which Python values are mutable,
hashable and truthy, instead of just telling them.

Use this sample list:

```python
SAMPLES = [5, 3.14, "abc", (1, 2), [1, 2], {"a": 1}, {1, 2}, frozenset({1, 2}), None, True, 0, ""]
```

## Features

| Feature | Owner | File | What it must do |
|---------|-------|------|-----------------|
| **F1 – Inspector table** | Member 1 | `inspector.py` | For each value print one f-string row: value, type name (`type(v).__name__`), Mutable? (Yes if `type(v) in (list, dict, set)`), Hashable? (try `hash(v)`, `except TypeError` → No), Truthy? (`bool(v)`). |
| **F2 – Experiments** | Member 2 (team lead) | `experiments.py` | Print **SAME** or **CHANGED** (not raw ids) for: (a) `x = 10; x += 1` – does `id(x)` change? (b) `lst = [1]; lst += [2]` – does `id(lst)` change? (c) `a = [1, 2]; b = [1, 2]` – print `a == b` and `a is b`. (d) the grid trap: `grid = [[0] * 3] * 3; grid[0][0] = 9` → print the grid, then build it correctly with a `for` loop and show only one cell changes. |
| **Integration** | Team lead | `main.py` | Menu loop: `1` inspector table, `2` experiments, `3` quiz, `0` exit. **Quiz** (lead writes it): ask "Is a tuple mutable? (y/n)" for 5 types, count the score. |

## Expected results (rows to check)

```
[1, 2]        list       Mutable: Yes  Hashable: No   Truthy: True
(1, 2)        tuple      Mutable: No   Hashable: Yes  Truthy: True
frozenset({1, 2}) frozenset Mutable: No Hashable: Yes Truthy: True
None          NoneType   Mutable: No   Hashable: Yes  Truthy: False
""            str        Mutable: No   Hashable: Yes  Truthy: False
Experiment a: CHANGED   b: SAME   c: True False
Grid trap   : [[9, 0, 0], [9, 0, 0], [9, 0, 0]]
Grid fixed  : [[9, 0, 0], [0, 0, 0], [0, 0, 0]]
```

## Team size changes
- **3 people:** Member 3 owns the quiz as F3.
- **4 people:** add F4 – "Copy lab": show `.copy()` vs `copy.deepcopy()` on `[[1, 2], [3, 4]]`, changing an inner list each time.
