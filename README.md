# Anudip-Python-Day3
Lab details of all Anudip CoE - python Day 3 sessions

## Gist – what Day 3 covered

**Topic: Python objects and mutability.** Motto: *build mutable · share immutable*.

1. **Every object = value + type + identity.** A variable is only a *name* (label) that points to an object. `type(x)` shows the type, `id(x)` shows the identity.
2. **Immutable types** – `int`, `float`, `bool`, `complex`, `str`, `tuple`, `frozenset`, `bytes`, `range`, `None`. "Changing" them builds a **new** object (the id changes).
3. **Mutable types** – `list`, `dict`, `set`, `bytearray`, `deque`, `array` and your own class instances. They change **in place** (the id stays the same).
4. **Two names, one object** – `b = a` does not copy. Mutability only bites when an object is shared.
5. **Does Python reuse values?** `==` compares values, `is` compares identity. CPython pre-builds a few immutable objects (ints −5…256, `True`/`False`, `None`, short strings, `()`), but it never looks up an existing object by value. Use `is` only with `None`.
6. **Truthiness** – `0`, `""`, `[]`, `None` (and other empty things) are `False`.
7. **Operators** – identity (`is`, `is not`), membership (`in`, `not in`), logical (`and`, `or`, `not`); revision of `bin()` / `hex()`.
8. **Build or share?** – grow data in a mutable type, hand it out as an immutable one (e.g. tuple keys in a dict).
9. **First look at classes** – `Point`, `Dog`, `Account`.

Class discussion (shared chat): https://claude.ai/share/36334e86-a7e0-49a3-8425-fcf1a79a9664

## What is in this repository

| Path | What it is |
|------|------------|
| `Day3 - Python - classes.pdf` | Class slides: objects table, CPython caching table, mutable vs immutable table, class code |
| `Mutability Lab — Python objects, live.html` | Interactive page – open it in a browser and press the buttons |
| [`Day3_Structured/`](Day3_Structured) | 10 numbered lessons that follow the class, with PREDICT and TRY IT YOURSELF sections |
| [`Day3_DeepDive/`](Day3_DeepDive) | 5 deep-dive sessions: references, CPython caching, copying, hashability, common traps |

## Suggested order

1. Open the Mutability Lab page and play with it.
2. Work through `Day3_Structured` lessons 01 → 10.
3. Take the deep dives in `Day3_DeepDive` 01 → 05.

Previous day: [Anudip-Python-Day2](https://github.com/Aswath1986/Anudip-Python-Day2) · Next day: [Anudip-python-day4](https://github.com/Aswath1986/Anudip-python-day4)
