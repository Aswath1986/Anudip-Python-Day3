"""
==========================================================================
 Day 3 | Lesson 04 : The Identity Experiment
==========================================================================
 This is the same experiment as Section 1 of the "Mutability Lab" page.

 What you will learn
   1. How to TEST if a type is mutable using id()
   2. x += 1 on an int makes a NEW object
   3. x.append(9) on a list changes the SAME object

 Rule:  id changes      -> new box     -> IMMUTABLE
        id stays same   -> same box    -> MUTABLE

 Run this file :  python 04_identity_experiment.py
==========================================================================
"""

def experiment(label, x, operation):
    """Run an operation and report whether the id changed."""
    before = id(x)
    x = operation(x)
    after = id(x)
    if before == after:
        result = "SAME object  -> mutable"
    else:
        result = "NEW object   -> immutable"
    print(f"{label:<22} value now {x!r:<22} {result}")

# --------------------------------------------------------------------------
# 1. Immutable types: the operation always gives a NEW object
# --------------------------------------------------------------------------
def add_one(x):
    x += 1
    return x

def add_half(x):
    x += 0.5
    return x

def flip(x):
    return not x

def to_upper(x):
    return x.upper()

def add_to_tuple(x):
    x += (9,)
    return x

experiment("int    x += 1", 5, add_one)
experiment("float  x += 0.5", 2.5, add_half)
experiment("bool   x = not x", True, flip)
experiment("str    x = x.upper()", "hi", to_upper)
experiment("tuple  x += (9,)", (1, 2), add_to_tuple)

# --------------------------------------------------------------------------
# 2. Mutable types: the operation changes the SAME object
# --------------------------------------------------------------------------
def append_nine(x):
    x.append(9)
    return x

def set_first(x):
    x[0] = 99
    return x

def add_nine(x):
    x.add(9)
    return x

experiment("list   x.append(9)", [1, 2], append_nine)
experiment("list   x[0] = 99", [1, 2], set_first)
experiment("set    x.add(9)", {1, 2}, add_nine)

# --------------------------------------------------------------------------
# 3. The same thing, without a helper function
# --------------------------------------------------------------------------
x = 5
print(id(x))
x += 1
print(id(x))        # different -> int is immutable

x = [1, 2]
print(id(x))
x.append(9)
print(id(x))        # same -> list is mutable


# ==========================================================================
# PREDICT before you run!
#   For each line, will the id change?
#     x = "abc";   x += "d"
#     x = [1];     x += [2]        (careful! += on a list changes in place)
#     x = [1];     x = x + [2]     (+ always builds a new list)
#
# TRY IT YOURSELF
#   Add your own experiment() line for a dict: d["new"] = 1
# ==========================================================================
