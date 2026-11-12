"""
==========================================================================
 Day 3 | Deep Dive 02 : Inside CPython - Caching and Interning
==========================================================================
 Goes deeper than Lesson 06. Explains each row of the class table
 "What CPython pre-builds or shares".

 IMPORTANT: everything here is an IMPLEMENTATION DETAIL of CPython.
 It can change between versions. Real programs must use == for values.

 Run this file :  python deep_dive_02_cpython_caching_and_interning.py
==========================================================================
"""
import sys

def fresh_int(text):
    """Build an int at run time so the compiler cannot reuse a constant."""
    return int(text)

# --------------------------------------------------------------------------
# 1. int : -5 .. 256 are pre-built when Python starts
# --------------------------------------------------------------------------
for n in [-6, -5, 0, 256, 257]:
    shared = fresh_int(str(n)) is fresh_int(str(n))
    print(f"{n:>4} shared? {shared}")
#   -6 False  |  -5 True  |  0 True  |  256 True  |  257 False
# Why? Small numbers are used everywhere (loop counters, indexes), so
# keeping one copy saves memory and time.

# --------------------------------------------------------------------------
# 2. bool and None : singletons
# --------------------------------------------------------------------------
print((3 > 1) is True)        # True   - there is exactly one True
print(type(None)() is None)   # True   - NoneType() gives back the same None

# --------------------------------------------------------------------------
# 3. str : interning
# --------------------------------------------------------------------------
# Single characters and the empty string are shared.
s1 = "".join(["a"])
s2 = "".join(["a"])
print("single char shared?", s1 is s2)          # True

# Longer strings built at run time are NOT automatically shared ...
w1 = "".join(["hello", "_", "world"])
w2 = "".join(["hello", "_", "world"])
print("built strings shared?", w1 is w2)        # False

# ... but you can ask Python to intern them yourself.
w1 = sys.intern(w1)
w2 = sys.intern(w2)
print("after sys.intern?", w1 is w2)            # True
# Python interns names of variables, functions and attributes, which makes
# dictionary lookups of names very fast.

# --------------------------------------------------------------------------
# 4. bytes : single-byte values and b"" are shared
# --------------------------------------------------------------------------
print(bytes([65]) is bytes([65]))               # True
print(bytes([65, 66]) is bytes([65, 66]))       # False

# --------------------------------------------------------------------------
# 5. tuple / frozenset : only the EMPTY one is shared
# --------------------------------------------------------------------------
print(tuple([]) is tuple([]))                   # True
print(tuple([1]) is tuple([1]))                 # False
print(frozenset([]) is frozenset([]))           # depends on version: False on 3.13
# The class table says "shared in recent versions" - this line shows why
# you should never write code that depends on it.

# --------------------------------------------------------------------------
# 6. float, complex, range : nothing cached by value
# --------------------------------------------------------------------------
print(float("1.5") is float("1.5"))             # False
# CPython keeps a "free list" of recycled float memory - so a NEW float
# can get the SAME id as one that was just deleted. Same id at different
# times does not mean same object!
print(id(float("2.5")) == id(float("3.5")))     # often True - recycled memory

# --------------------------------------------------------------------------
# 7. Constant folding in a .py file
# --------------------------------------------------------------------------
a = 1000
b = 1000
print("1000 is 1000 in a file:", a is b)        # True here (same code object)
# Type the same two lines in the interactive shell and you usually get
# False. Same code, different answer -> never rely on "is" for values.


# ==========================================================================
# THINK ABOUT IT
#   Why is caching only safe for IMMUTABLE objects?
#   (Hint: what would happen if every empty list [] was the same object?)
# ==========================================================================
