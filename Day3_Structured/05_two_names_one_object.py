"""
==========================================================================
 Day 3 | Lesson 05 : Two Names, One Object (Aliasing)
==========================================================================
 This is Section 2 of the "Mutability Lab" page.

 What you will learn
   1. b = a does NOT copy. It adds a second label to the same object
   2. With a MUTABLE object, a change through b is seen through a
   3. With an IMMUTABLE object, b = b + ... moves only b
   4. How to make a real copy

 Run this file :  python 05_two_names_one_object.py
==========================================================================
"""

# --------------------------------------------------------------------------
# 1. list (mutable) - both names see the change
# --------------------------------------------------------------------------
a = [1, 2]
b = a              # second label, same list
b.append(3)        # change the list through b
print("a =", a)    # [1, 2, 3]   <- a sees it too!
print("a is b :", a is b)   # True

# --------------------------------------------------------------------------
# 2. str (immutable) - only b moves
# --------------------------------------------------------------------------
a = "hi"
b = a              # second label, same string
b = b + "!"        # builds a NEW string; only b moves to it
print("a =", a)    # hi          <- a is safe
print("b =", b)    # hi!
print("a is b :", a is b)   # False

# KEY IDEA: Mutability only matters when an object is SHARED.

# --------------------------------------------------------------------------
# 3. Making a real copy of a list
# --------------------------------------------------------------------------
a = [1, 2]
b = a.copy()       # also works: list(a)  or  a[:]
b.append(3)
print("a =", a)    # [1, 2]      <- not affected
print("b =", b)    # [1, 2, 3]
print("a is b :", a is b)   # False

# --------------------------------------------------------------------------
# 4. A real-life bug: shared shopping list
# --------------------------------------------------------------------------
my_list = ["milk", "bread"]
friends_list = my_list           # friend wanted their OWN list...
friends_list.append("chocolate")
print("My list:", my_list)       # ['milk', 'bread', 'chocolate']  surprise!


# ==========================================================================
# PREDICT before you run!
#   x = [10]
#   y = x
#   y[0] = 20
#   print(x)
#
#   p = 10
#   q = p
#   q = q + 5
#   print(p)
#
# TRY IT YOURSELF
#   Fix the shopping list bug in section 4 with .copy().
# ==========================================================================
