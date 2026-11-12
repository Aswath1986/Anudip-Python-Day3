# Day 3 – Deep Dive Sessions

Take these **after** the structured lessons. Each deep dive picks up one idea from class and
explains *why* Python behaves that way.

| # | File | Goes deeper into | Key ideas |
|---|------|------------------|-----------|
| 01 | `deep_dive_01_names_and_references.py` | Lessons 01, 05 | binding vs copying, reference counting (`sys.getrefcount`), `del`, passing objects to functions |
| 02 | `deep_dive_02_cpython_caching_and_interning.py` | Lesson 06 | each row of the "What CPython pre-builds or shares" table, `sys.intern`, free lists, constant folding |
| 03 | `deep_dive_03_shallow_vs_deep_copy.py` | Lesson 05 | `.copy()` vs `copy.deepcopy()`, the `[[0]*3]*3` grid trap |
| 04 | `deep_dive_04_hashability_and_dict_keys.py` | Lesson 09 | `hash()`, why lists can't be dict keys, `frozenset`, the `t[1] += [5]` tuple puzzle |
| 05 | `deep_dive_05_augmented_assignment_and_default_args.py` | Lesson 04 | `x += y` vs `x = x + y`, the mutable default argument bug |

Every file ends with a **THINK ABOUT IT** question for class discussion.

> Deep Dive 02 explores CPython *implementation details*. Results can differ between Python
> versions (the comments note where). The rule never changes: compare values with `==`, use `is`
> only for `None`.

```bash
cd Day3_DeepDive
python deep_dive_01_names_and_references.py
```
