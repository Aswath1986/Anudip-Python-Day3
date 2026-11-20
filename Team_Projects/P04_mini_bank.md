# P04 – Mini Bank with PIN Login

**Team size:** 3  **Builds on:** Day 2 Lesson 07 (PIN check with while), Lesson 10 (walrus), Day 3 Lesson 10 (`Account` class), Lesson 05 (two names, one object)

## Problem statement
Extend the `Account` class from Day 3 Lesson 10 into a small bank counter program: a customer
logs in with a PIN, deposits, withdraws, transfers money and sees a mini statement.

## Features

| Feature | Owner | File | What it must do |
|---------|-------|------|-----------------|
| **F1 – Account class** | Member 1 | `account.py` | `class Account` with `holder`, `balance`, `history` (a list, created inside `__init__`). `deposit(amount)` only if `amount > 0`. `withdraw(amount)` prints "Not enough balance!" if `amount > self.balance`. Every successful action appends a line such as `"+500"` or `"-300"` to `history`. `statement()` prints the last 5 entries and the balance. |
| **F2 – Secure login** | Member 2 | `login.py` | PIN is `4321`. Allow at most 3 tries with a `while` loop and walrus: `while tries < 3 and (pin := input("PIN: ")) != "4321":`. After 3 wrong tries print "Card blocked" and stop. |
| **F3 – Transfer & joint account** | Member 3 (team lead) | `transfer.py` | `transfer(src, dst, amount)` moves money only when `src.balance >= amount and amount > 0`. Joint account demo: `joint = ravi` then deposit through `joint` – show that `ravi` sees it and `joint is ravi` is True. Then create a real second account and show `is` is False. |
| **Integration** | Team lead | `main.py` | Login first; if it succeeds, menu loop: deposit, withdraw, transfer, statement, exit. |

## Sample run (must match)

```
Ravi opens with 1000, Sita opens with 500
Ravi deposit 500       -> balance 1500
Ravi withdraw 2000     -> Not enough balance!
Ravi withdraw 300      -> balance 1200
Transfer 200 Ravi→Sita -> Ravi 1000, Sita 700
Ravi statement         -> +500, -300, -200 | balance 1000
Wrong PIN 3 times      -> Card blocked
```

## Team size changes
- **2 people:** Member 1 = F1, Member 2 (lead) = F2 + F3.
- **4 people:** add F4 – "Interest & fees": add 4 % yearly interest (`balance * 4 / 100`) and a ₹10 fee when a withdrawal leaves less than ₹500, recorded in `history`.
