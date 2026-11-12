"""
==========================================================================
 Day 3 | Deep Dive 01 : Names, References and Garbage Collection
==========================================================================
 Goes deeper than Lessons 01 and 05.

 What you will learn
   1. Assignment NEVER copies - it binds a name to an object
   2. Reference counting: how Python knows when to delete an object
   3. del removes a NAME, not the object
   4. Passing an object to a function passes a reference
      ("call by object reference")

 Run this file :  python deep_dive_01_names_and_references.py
==========================================================================
"""
import sys

# --------------------------------------------------------------------------
# 1. Assignment binds - picture it as arrows
# --------------------------------------------------------------------------
#   a = [1, 2]        a ──►  [1, 2]
#   b = a             a ──►  [1, 2]  ◄── b
#   a = [9]           a ──►  [9]         [1, 2] ◄── b
a = [1, 2]
b = a
a = [9]
print("a =", a, " b =", b)          # a = [9]  b = [1, 2]

# --------------------------------------------------------------------------
# 2. Reference counting
# --------------------------------------------------------------------------
# Every object keeps a counter of how many references point at it.
# When the counter reaches 0, CPython frees the memory immediately.
# sys.getrefcount() shows the count (+1, because the function argument
# itself is a temporary reference). Exact numbers can differ between
# Python versions - watch how the count goes UP and DOWN.
data = [1, 2, 3]
print("refs:", sys.getrefcount(data))     # 2  (data + the argument)
alias = data
print("refs:", sys.getrefcount(data))     # 3
del alias
print("refs:", sys.getrefcount(data))     # 2 again

# --------------------------------------------------------------------------
# 3. del removes the LABEL only
# --------------------------------------------------------------------------
x = [10, 20]
y = x
del x               # the name x is gone ...
print(y)            # [10, 20]  ... but the list still lives (y points to it)
try:
    print(x)
except NameError as error:
    print("NameError:", error)

# --------------------------------------------------------------------------
# 4. Functions receive references
# --------------------------------------------------------------------------
def add_item(items):
    items.append("new")       # MUTATES the caller's object

def replace_items(items):
    items = ["fresh"]         # only rebinds the LOCAL name

shopping = ["rice"]
add_item(shopping)
print(shopping)               # ['rice', 'new']   <- changed
replace_items(shopping)
print(shopping)               # ['rice', 'new']   <- NOT changed

def increment(n):
    n += 1                    # int is immutable -> a new local object
    return n

count = 5
increment(count)
print(count)                  # 5   (use: count = increment(count))


# ==========================================================================
# THINK ABOUT IT
#   Why does add_item() change the caller's list but replace_items() does
#   not? Draw the arrows for both.
# ==========================================================================
