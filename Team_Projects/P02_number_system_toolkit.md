# P02 – Number System & Secret Message Toolkit

**Team size:** 3  **Builds on:** Day 2 Lesson 03 (`bin`, `oct`, `hex`, `int(x, base)`, `ord`, `chr`), Lesson 05 (for + range), Day 3 Lesson 08 (`in`, `not in`)

## Problem statement
A computer-science club wants one small tool that converts numbers between bases and
hides short messages using character codes.

## Features

| Feature | Owner | File | What it must do |
|---------|-------|------|-----------------|
| **F1 – Decimal converter** | Member 1 | `converter.py` | Read a whole number and print its binary, octal and hex **without** the `0b`/`0o`/`0x` prefix (cut it off with `[2:]`). Then read `start` and `stop` and print a neat table for `range(start, stop)` using f-strings. |
| **F2 – Any base to decimal** | Member 2 | `to_decimal.py` | Read a value and a base (2, 8 or 16). Check **every** character with a `for` loop and `in` against the allowed digits (`"01"`, `"01234567"`, `"0123456789abcdef"`). If one is wrong print the bad digit; otherwise print `int(value, base)`. |
| **F3 – Secret message** | Member 3 (team lead) | `secret.py` | Caesar shift for capital letters A–Z using `ord()`, `chr()` and `%` to wrap Z back to A: `chr((ord(c) - 65 + shift) % 26 + 65)`. Leave spaces unchanged. Option to encode and to decode (shift the other way). Also print each letter's ASCII code. |
| **Integration** | Team lead | `main.py` | Menu loop with walrus: `1` decimal converter, `2` any base to decimal, `3` secret message, `0` exit. |

## Sample runs (must match)

```
F1  25           -> binary 11001, octal 31, hex 19
F2  ff  base 16  -> 255
F2  102 base 2   -> Invalid digit '2' for base 2
F3  HELLO shift 3 encode -> KHOOR      codes: 72 69 76 76 79
F3  KHOOR shift 3 decode -> HELLO
```

## Team size changes
- **2 people:** one person does F1 + F2 (both are number conversions).
- **4 people:** add F4 – "Text to binary": print each character as 8-bit binary, padding `bin(ord(c))[2:]` on the left with `"0" * (8 - len(b))`. `Hi` → `01001000 01101001`.
