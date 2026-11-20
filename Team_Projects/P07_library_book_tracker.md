# P07 – Library Book Tracker

**Team size:** 3  **Builds on:** Day 3 Lesson 10 (classes), Lesson 05 (aliasing), Lesson 08 (logical and membership operators), Deep Dive 05 (mutable default argument bug)

## Problem statement
The training centre library wants to track which books are on the shelf and who has borrowed
what. A member may hold at most **2** books.

## Features

| Feature | Owner | File | What it must do |
|---------|-------|------|-----------------|
| **F1 – Book catalogue** | Member 1 | `book.py` | `class Book` with `isbn`, `title`, `author`, `available = True`. `catalogue = {}` maps isbn → Book. Add a book (reject a duplicate isbn with `in`). Search by a word in the title, ignoring case (`word.lower() in book.title.lower()`). |
| **F2 – Member class (bug hunt)** | Member 2 | `member.py` | Start from this **buggy** code given by the trainer: `def __init__(self, name, borrowed=[]):`. Create two members, let one borrow a book, print both lists and show the bug (both lists change, `m1.borrowed is m2.borrowed` → True). Fix it with `borrowed=None` and `if borrowed is None: borrowed = []`. Commit the buggy demo and the fix as **separate commits**. |
| **F3 – Borrow / return desk** | Member 3 (team lead) | `desk.py` | `borrow(member, isbn)` succeeds only if `isbn in catalogue and book.available and len(member.borrowed) < 2`; otherwise print the exact reason. `return_book(member, isbn)` only if `isbn in member.borrowed`. Keep `available` up to date. |
| **Integration** | Team lead | `main.py` | Menu loop: add book, search, add member, borrow, return, list books with status, exit. |

## Sample run (must match)

```
Books : B1 "Python Basics", B2 "Learn SQL", B3 "Python Projects"
Search "python"          -> B1 Python Basics, B3 Python Projects
Ravi borrows B1          -> OK
Sita borrows B1          -> Not available
Ravi borrows B2, then B3 -> OK, then "Limit reached (2 books)"
Ravi returns B1          -> OK, B1 available again
Sita borrows B9          -> No such book
Bug demo (before fix)    -> Sita's list also shows ['B1'], same object: True
After fix                -> Sita's list is [], same object: False
```

## Team size changes
- **2 people:** Member 1 = F1 + F2, Member 2 (lead) = F3.
- **4 people:** add F4 – "Reports": books currently out, the member holding the most books, and the count of available books.
