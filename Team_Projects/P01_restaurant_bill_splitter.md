# P01 – Restaurant Bill Splitter

**Team size:** 2  **Builds on:** Day 2 Lesson 09 (bill calculator, "MAKE: Restaurant Bill"), Lessons 07 and 10 (while, walrus), Day 3 Lesson 09 (build with a dict)

## Problem statement
A group of friends eats at a small hotel. The waiter wants a program that takes the order, adds
GST and tip, and tells each friend how much to pay.

The menu is fixed:

```python
MENU = {"idli": 40, "dosa": 70, "coffee": 25, "meals": 120}
```

## Features

| Feature | Owner | File | What it must do |
|---------|-------|------|-----------------|
| **F1 – Order taker** | Member 1 (team lead) | `order.py` | Use `while (item := input("Item: ")) != "done":` to read items. Reject items that are `not in` MENU. Read a quantity for each item and add it to an `order` dict with `+=` (ordering dosa twice adds up). Print the order and the food total. |
| **F2 – Bill and split** | Member 2 | `bill.py` | Given the food total: GST = 5 %, tip = 15 % of the food total, grand total = food + GST + tip. Read the number of people. Print the share per person rounded to 2 decimals, then, using `int(total) // people` and `int(total) % people`, print the whole-rupee share and the leftover rupees. Reject `people <= 0`. |
| **Integration** | Team lead | `main.py` | Menu: `1` take order, `2` show bill and split, `0` exit, in a `while` loop. Option 2 before option 1 must print "No order yet" (use truthiness: `if not order:`). |

## Sample run (must match)

```
Item: dosa   Qty: 2
Item: coffee Qty: 3
Item: dosa   Qty: 1
Item: done
Order      : {'dosa': 3, 'coffee': 3}
Food total : 285
GST (5%)   : 14.25
Tip (15%)  : 42.75
Grand total: 342.0
People     : 4
Each pays  : 85.5
Whole rupees each: 85, leftover: 2
```

## Team size changes
- **3 people:** split F2 into F2 (GST + tip) and F3 (split among people).
- **4 people:** also add F4 – "Today's sales": keep a list of every finished bill's grand total and print count, total and highest.
