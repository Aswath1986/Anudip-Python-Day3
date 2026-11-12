"""
==========================================================================
 Day 3 | Lesson 06 : Does Python Reuse Values?  ( == vs is )
==========================================================================
 This is Section 3 of the "Mutability Lab" page and the CPython table.

 What you will learn
   1. ==  compares VALUES        is  compares IDENTITY (same object?)
   2. CPython keeps some immutable objects ready-made and shares them
   3. Why you must NEVER use "is" to compare numbers or strings

 Run this file :  python 06_does_python_reuse_values.py
==========================================================================
"""

# --------------------------------------------------------------------------
# 1. == vs is
# --------------------------------------------------------------------------
x = 5
y = x
print(x == y)      # True  -> same value
print(x is y)      # True  -> same object (y = x copies the LABEL)

a = [1, 2]
b = [1, 2]
print(a == b)      # True  -> same value
print(a is b)      # False -> two different list objects

# --------------------------------------------------------------------------
# 2. What CPython pre-builds or shares (table from class)
# --------------------------------------------------------------------------
#   int        -5 to 256, one object each (the "small int cache")
#   bool       exactly one True and one False
#   None       a single None object
#   str        single characters and short identifier-like strings are
#              "interned"; the empty string "" is shared
#   bytes      single-byte values 0 to 255, plus the empty b""
#   tuple      the empty tuple () is shared
#   float      nothing cached by value
#   frozenset  the empty frozenset() is shared (recent versions)
#   complex    nothing cached
#   range      nothing cached

# Small ints are shared. int("...") builds the number at RUN time,
# so we are sure Python did not just reuse a constant from the source code.
m = int("100")
n = int("100")
print("100 :", m is n)     # True  -> inside -5..256, shared

m = int("1000")
n = int("1000")
print("1000:", m is n)     # False -> outside the cache, two objects

# Singletons
print(bool(1) is True)     # True  -> there is only ONE True
print(tuple([]) is tuple())  # True  -> only ONE empty tuple

# --------------------------------------------------------------------------
# 3. The common guess is WRONG
# --------------------------------------------------------------------------
# Guess: "the value 1000 already exists, so Python points y at it."
# Truth: Python never searches memory for an equal value. Sharing happens
#        only because of (a) y = x, or (b) a small built-in cache.
#
# NOTE: in a .py file the compiler may fold two equal literals
#       (x = 1000; y = 1000) into one object, so "x is y" can be True.
#       In the interactive shell it is usually False. That is exactly why
#       "is" on numbers/strings gives unreliable answers.

# --------------------------------------------------------------------------
# 4. The golden rule
# --------------------------------------------------------------------------
#   Use  ==  to compare values (numbers, strings, lists ...)
#   Use  is  ONLY with None:   if result is None:
result = None
print(result is None)      # True


# ==========================================================================
# PREDICT before you run!
#   print(int("256") is int("256"))      print(int("257") is int("257"))
#   print([] is [])                      print([] == [])
#
# TRY IT YOURSELF
#   Open the Python shell (type python) and try:  x = 1000;  y = 1000;
#   then  x is y  on two separate lines. Compare with this file.
# ==========================================================================
