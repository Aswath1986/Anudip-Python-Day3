# Team Practice Projects – Day 2 + Day 3

Eight team projects that use **only what Day 2 and Day 3 taught**:
`print` / f-strings / `input()`, number systems and `ord()`/`chr()`, lists, `for` + `range`,
`while`, arithmetic / relational / assignment / logical / identity / membership operators,
walrus `:=`, simple `if / elif / else`, mutable vs immutable types (list, dict, set, tuple,
frozenset), aliasing and `.copy()` / `copy.deepcopy()`, `==` vs `is`, truthiness,
`try / except TypeError` (Lesson 09), and classes with `__init__`, `self` and methods (Lesson 10).

> Each feature lives in its own file as a **class** (Day 3 Lesson 10) or a small **function**
> made with `def` (seen in Deep Dive 05). Trainers: if functions are not taught yet, ask teams to
> write every feature as a class with methods.

## The projects

| # | Project | Team size | Main concepts |
|---|---------|-----------|---------------|
| P01 | [Restaurant Bill Splitter](P01_restaurant_bill_splitter.md) | **2** | dict, while + walrus, arithmetic, `//` `%` |
| P02 | [Number System & Secret Message Toolkit](P02_number_system_toolkit.md) | **3** | `bin` `oct` `hex` `int(x, base)` `ord` `chr`, `in` |
| P03 | [Student Marks Register](P03_student_marks_register.md) | **4** | class, dict of objects, truthiness, deepcopy |
| P04 | [Mini Bank with PIN Login](P04_mini_bank.md) | **3** | class `Account`, PIN while-loop, aliasing |
| P05 | [Object Inspector (Mutability Detective)](P05_object_inspector.md) | **2** | type, mutable vs immutable, hashable, `is` |
| P06 | [Attendance & Seating Planner](P06_attendance_seating.md) | **4** | tuple roster, sets, nested lists, tuple keys |
| P07 | [Library Book Tracker](P07_library_book_tracker.md) | **3** | two classes, mutable-default-argument bug |
| P08 | [Shopping Cart & Checkout](P08_shopping_cart_checkout.md) | **4** | dict of tuples, GST + discount rules, receipts |

Every project lists its features **F1, F2, …**. One person owns one feature. Each project file
also says how to run it with a smaller or bigger team, so any project can go to a team of 2, 3 or 4.

## Roles

| Role | Who | Does |
|------|-----|------|
| **Feature owner** | every team member (lead included) | Builds one feature on their own branch, opens a PR to the team branch |
| **Team lead** | one member of each team | Reviews and runs every feature PR, merges them, writes `main.py` (the menu that joins the features), fixes merge conflicts, opens the team PR to the project lead |
| **Project lead** | one trainee per batch (or a co-trainer) | Reviews the team PRs from all teams, checks the folder and commit rules, merges into `develop`, opens the final PR to `main` |
| **Trainer / facilitator** | trainer | Reviews the commit history and PRs, approves and merges into `main` |

## Git workflow

```
feature branch ──PR──▶ team branch ──PR──▶ develop ──PR──▶ main
(member)              (team lead)         (project lead)    (trainer approves)
```

1. Project lead creates `develop` from `main`.
2. Team lead creates the team branch from `develop`: `team-01/dev`, and adds the project folder
   `Team_Projects/team-01_P03/` with an empty `main.py` and a `README.md` listing who owns what.
3. Each member creates a feature branch from the team branch: `team-01/f2-register`.
4. Members commit **small and often** (at least 3 commits each), push, and open a PR into
   `team-01/dev`. PR description: which feature, how to run it, a screenshot of a sample run.
5. Team lead pulls the branch, **runs it**, comments on anything wrong, and merges only when it works.
   Every member adds their menu option to `main.py`, so the team **will** get a merge conflict
   there. The lead resolves it. That is part of the exercise.
6. Team lead runs the full program from `main.py`, then opens a PR `team-01/dev → develop`.
7. Project lead reviews and merges the team PRs, then opens `develop → main`.
8. Trainer reviews the commits and approves the merge to `main`.

**Commit message format:** `F2: add duplicate-name check` (feature number + what changed).
**Never commit straight to** `team-xx/dev`, `develop` or `main`.

## Trainer evaluation checklist

| Area | What to look for | Marks |
|------|------------------|-------|
| Feature works | Sample input in the project file gives the expected output | 30 |
| Uses the target concepts | The concepts named in the feature are actually used | 20 |
| Commit history | ≥ 3 meaningful commits per member, correct message format, no giant single commit | 15 |
| Pull request | Clear description, screenshot, linked to the right branch | 10 |
| Team lead review | Real review comments, conflict in `main.py` resolved, integrated program runs | 15 |
| Project lead review | Folder and branch rules followed before merging to `develop` | 10 |
