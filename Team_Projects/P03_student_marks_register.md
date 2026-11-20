# P03 – Student Marks Register

**Team size:** 4  **Builds on:** Day 3 Lesson 10 (classes), Lesson 07 (truthiness), Lesson 09 (build mutable, share immutable), Deep Dive 03 (shallow vs deep copy)

## Problem statement
A class teacher wants to enter marks for each student, see grades and the topper, and hand a
"final result" to the principal that **cannot be changed by accident**.

## Features

| Feature | Owner | File | What it must do |
|---------|-------|------|-----------------|
| **F1 – Student class** | Member 1 | `student.py` | `class Student` with `name` and `marks` (start as `[]` **inside** `__init__`). Methods: `add_mark(m)` accepts only `0 <= m <= 100` (use `and` or chained compare), `average()` returns `0` when there are no marks (`if not self.marks:`), `grade()` → A (≥ 90), B (≥ 75), C (≥ 50), F otherwise. |
| **F2 – Register entry** | Member 2 | `register.py` | `register = {}` maps name → Student. Add a student (reject a name already `in` the register). Add marks for a student with a `while` loop that stops on `"done"`. |
| **F3 – Reports** | Member 3 | `reports.py` | Print an f-string table (Name, Marks, Average to 2 decimals, Grade), the topper, the class average and the count of students who **passed** (average ≥ 50 **and** no single mark below 35). |
| **F4 – Final result snapshot** | Member 4 (team lead) | `snapshot.py` | Make `final_result` as a **tuple** of `(name, average, grade)` tuples. Show the alias bug: `backup = register` then change a mark → backup changes too (`backup is register` → True). Fix it with `copy.deepcopy()` and prove with `is` that it is a different object and does not change. |
| **Integration** | Team lead | `main.py` | Menu loop: add student, add marks, show report, freeze final result, exit. |

## Sample data and expected report

```
Ravi  [78, 80, 92]  avg 83.33  B
Sita  [91, 95, 88]  avg 91.33  A
Arun  [45, 60, 30]  avg 45.0   F
Topper        : Sita
Class average : 73.22
Passed        : 2
add_mark(105) -> "Invalid mark"
```

## Team size changes
- **3 people:** Member 1 = F1, Member 2 = F2, Member 3 (lead) = F3 + F4.
- **2 people:** Member 1 = F1 + F2, Member 2 (lead) = F3 + F4.
