"""
==========================================================================
 Day 3 | Deep Dive 05 : Two Famous Traps - "+=" and Default Arguments
==========================================================================
 Goes deeper than Lesson 04.

 What you will learn
   1. x += y  is NOT always the same as  x = x + y
   2. The mutable default argument bug
   3. The fix: use None as the default

 Run this file :  python deep_dive_05_augmented_assignment_and_default_args.py
==========================================================================
"""

# --------------------------------------------------------------------------
# 1. += on a list changes IN PLACE,  + builds a NEW list
# --------------------------------------------------------------------------
a = [1, 2]
b = a
a += [3]                 # list.__iadd__ -> mutates the same list
print(b, a is b)         # [1, 2, 3] True

a = [1, 2]
b = a
a = a + [3]              # list.__add__ -> builds a new list
print(b, a is b)         # [1, 2] False

# For IMMUTABLE types there is no in-place version, so += always builds
# a new object:
s = "hi"
t = s
s += "!"
print(t, s is t)         # hi False

# --------------------------------------------------------------------------
# 2. The mutable default argument bug
# --------------------------------------------------------------------------
# The default value is created ONCE, when "def" runs - not on every call.
def add_student_bad(name, group=[]):
    group.append(name)
    return group

print(add_student_bad("Ravi"))   # ['Ravi']
print(add_student_bad("Sita"))   # ['Ravi', 'Sita']   <- surprise!

# --------------------------------------------------------------------------
# 3. The fix
# --------------------------------------------------------------------------
def add_student_good(name, group=None):
    if group is None:            # "is None" - the correct use of "is"
        group = []               # a NEW list on every call
    group.append(name)
    return group

print(add_student_good("Ravi"))  # ['Ravi']
print(add_student_good("Sita"))  # ['Sita']

# Immutable defaults (numbers, strings, tuples, None) are always safe.


# ==========================================================================
# THINK ABOUT IT
#   Write a function log(message, history=None) that keeps a list of
#   messages. Call it 3 times with and without passing a history.
# ==========================================================================
