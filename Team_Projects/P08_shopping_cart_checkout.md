# P08 – Shopping Cart & Checkout

**Team size:** 4  **Builds on:** Day 2 Lesson 09 (bill calculator + logical operator preview), Day 3 Lesson 09 (build mutable, share immutable), Lesson 05 (`.copy()`), Lesson 07 (truthiness)

## Problem statement
Turn the Day 2 shopping-bill calculator into a real checkout counter: pick products, apply
GST and the discount rules from the Day 2 "preview" comment, and print a receipt.

```python
PRODUCTS = {"P1": ("Pen", 50), "P2": ("Notebook", 120), "P3": ("Bag", 900)}   # values are tuples
VALID_COUPONS = ("SAVE10", "WELCOME")
```

## Features

| Feature | Owner | File | What it must do |
|---------|-------|------|-----------------|
| **F1 – Cart builder** | Member 1 | `cart.py` | `cart = {}` maps code → quantity. Loop with `while (code := input("Code: ")) != "done":`, reject codes `not in PRODUCTS`, add quantity with `+=`. Print the cart with product names. |
| **F2 – Bill rules** | Member 2 | `bill.py` | `subtotal`; GST 18 %; `big_order = subtotal >= 1000`; `gets_discount = (big_order and is_member) or has_coupon` → 10 % off the bill after GST; `free_shipping = big_order and not (total_qty > 10)`, otherwise add ₹50 shipping. Final amount rounded to 2 decimals. |
| **F3 – Coupon check** | Member 3 | `coupon.py` | Ask for a coupon up to 3 times. Empty input means "no coupon" (`if not code:`). Check with `in VALID_COUPONS` – case matters, so `save10` is invalid. Return `True`/`False` for `has_coupon`. |
| **F4 – Receipt & order history** | Member 4 (team lead) | `receipt.py` | Print an aligned receipt with f-strings. Save the order to `order_history` as a **tuple** of `(name, qty, line_total)` tuples. Show the alias bug first: `history.append(cart)` then `cart.clear()` empties the saved order; fix it with `cart.copy()` or a tuple. |
| **Integration** | Team lead | `main.py` | Menu loop: add to cart, view cart, checkout (coupon → bill → receipt), view history, exit. Checkout with an empty cart prints "Cart is empty". |

## Sample run (must match)

```
Cart          : Bag x1, Pen x2
Subtotal      : 1000
GST (18%)     : 180.0
Bill          : 1180.0
Member?       : yes   Coupon: (blank)
Discount 10%  : applied -> 1062.0
Shipping      : free
Final amount  : 1062.0

Same cart, not a member, coupon "save10" (lowercase) -> invalid, no discount
-> Final amount 1180.0
```

## Team size changes
- **3 people:** Member 2 does F2 + F3.
- **2 people:** Member 1 = F1 + F3, Member 2 (lead) = F2 + F4.
