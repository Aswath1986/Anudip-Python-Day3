# Day 3 – Structured Lessons

These files go over what we covered in the Day 3 class (the **Python objects / mutability** slides in
`Day3 - Python - classes.pdf` and the interactive **Mutability Lab** page) in a clear order.
Go through them **in number order**. Each lesson uses only what the lessons before it taught.

| # | File | Concept | Comes from |
|---|------|---------|------------|
| 01 | `01_what_is_an_object.py` | value, type, identity, name; `type()`, `id()` | PDF p.1 (Objects table) |
| 02 | `02_immutable_types.py` | int, float, bool, complex, str, tuple, frozenset, bytes, range, None | PDF p.2 (Immutable column) |
| 03 | `03_mutable_types.py` | list, dict, set, bytearray, deque, array, class instances | PDF p.2 (Mutable column) |
| 04 | `04_identity_experiment.py` | does `id()` change? → immutable vs mutable | Mutability Lab §1 |
| 05 | `05_two_names_one_object.py` | aliasing: `b = a`, `.copy()` | Mutability Lab §2 |
| 06 | `06_does_python_reuse_values.py` | `==` vs `is`, CPython caching table | Mutability Lab §3, PDF p.1 |
| 07 | `07_truthiness_bool.py` | `bool(0)`, `bool([])`, `bool("")`, `bool(None)` | PDF p.3 (class code) |
| 08 | `08_identity_membership_logical_operators.py` | `is` / `is not`, `in` / `not in`, `and` / `or` / `not`, `bin()`, `hex()` | PDF p.3 (class code) |
| 09 | `09_build_or_share_mini_project.py` | build with mutable, share as immutable (PRIMM) | Mutability Lab §4 |
| 10 | `10_classes_intro.py` | `class`, `__init__`, `self`, methods: `Point`, `Dog`, `Account` | PDF p.2 (user class instance) |

## How each lesson is laid out

1. **What you will learn**: the goals for the lesson.
2. **Numbered sections**: short explanations followed by code you can run.
3. **PREDICT before you run!**: write down what you expect, then check by running it.
4. **TRY IT YOURSELF**: small exercises to practise.

## Running a lesson

```bash
cd Day3_Structured
python 01_what_is_an_object.py
```

`id()` numbers are different on every computer and every run. What matters is whether
two ids are **the same** or **different**.

When you finish, go on to the deep dives in [`../Day3_DeepDive`](../Day3_DeepDive).
