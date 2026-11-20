# P06 – Attendance & Seating Planner

**Team size:** 4  **Builds on:** Day 3 Lesson 09 (MAKE: class attendance, tuple keys), Lesson 08 (`in`, `not in`), Deep Dive 03 (nested list trap), Deep Dive 04 (hashable keys)

## Problem statement
A trainer wants to mark attendance, see who is absent, seat the present students in a grid
and keep a weekly attendance record.

```python
CLASS_ROSTER = ("Asha", "Bala", "Chitra", "Dev", "Esha", "Farid")   # shared → tuple
WEEK_DAYS = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat")
```

## Features

| Feature | Owner | File | What it must do |
|---------|-------|------|-----------------|
| **F1 – Mark attendance** | Member 1 | `attendance.py` | Build a `present` **list** with `while (name := input("Name: ")) != "done":`. Reject names `not in CLASS_ROSTER` ("Not in this class") and names already marked ("Already marked"). Return the list frozen as a **tuple**. |
| **F2 – Absentee report** | Member 2 | `absentees.py` | Use sets: `set(CLASS_ROSTER) - set(present)`. Print absentees in alphabetical order (`sorted()`), the present count and the percentage to 2 decimals. Print "Full attendance!" when the absent set is empty (truthiness). |
| **F3 – Seating grid** | Member 3 | `seating.py` | Read rows and columns. Build the grid **correctly** with a `for` loop (one new list per row), fill present students row by row, `"-"` for empty seats. In a comment, explain why `[["-"] * cols] * rows` would be wrong. Print "Not enough seats" if `rows * cols < len(present)`. |
| **F4 – Weekly record** | Member 4 (team lead) | `weekly.py` | `record = {}` with keys `(day, period)` tuples and values the frozen `present` tuple. Reject days `not in WEEK_DAYS`. Look up a day + period. Show, with `try / except TypeError`, that `["Mon", 1]` cannot be a key. |
| **Integration** | Team lead | `main.py` | Menu loop: mark attendance, absentee report, seating, save to weekly record, look up record, exit. |

## Sample run (must match)

```
Present entered : Asha, Dev, Zara, Esha, Asha, Bala, done
                  Zara -> Not in this class,  Asha (2nd) -> Already marked
Present         : ('Asha', 'Dev', 'Esha', 'Bala')
Absent          : Chitra, Farid
Attendance      : 4/6 = 66.67%
Seating 2 x 3   : Asha  Dev  Esha
                  Bala  -    -
record[("Mon", 1)] -> ('Asha', 'Dev', 'Esha', 'Bala')
```

## Team size changes
- **3 people:** Member 1 = F1 + F2, Member 2 = F3, Member 3 (lead) = F4.
- **2 people:** Member 1 = F1 + F2, Member 2 (lead) = F3 + F4.
