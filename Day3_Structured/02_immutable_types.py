"""
==========================================================================
 Day 3 | Lesson 02 : Immutable Types (cannot be changed in place)
==========================================================================
 What you will learn
   1. What "immutable" means
   2. The immutable types: int, float, bool, complex, str, tuple,
      frozenset, bytes, range, None
   3. What happens when you try to change one

 Run this file :  python 02_immutable_types.py
==========================================================================
"""

# --------------------------------------------------------------------------
# 1. Immutable = once the object is made, its VALUE can never change.
# --------------------------------------------------------------------------
# To get a "new value" Python must build a NEW object.

# --------------------------------------------------------------------------
# 2. A tour of the immutable types (examples from the class table)
# --------------------------------------------------------------------------
print(42, -7, 0, 10**100)                  # int   (any size!)
print(3.14, -0.5, 2.0, 1e-9)               # float
print(True, False)                         # bool
print(3+4j, 2j, complex(1, -2))            # complex  (j is the imaginary part)
print("hello", "a", "", "नमस्ते")           # str   (any language - Unicode)
print((1, 2, 3), ("x", 5), (), (7,))       # tuple (note: (7,) needs a comma)
print(frozenset({1, 2}), frozenset("ab"))  # frozenset (a set that is frozen)
print(b"hi", b"\x00\xff", bytes(3))        # bytes (numbers 0-255)
print(range(10), list(range(2, 20, 2)))    # range
print(None)                                # None (the only NoneType value)

# --------------------------------------------------------------------------
# 3. Try to change a str -> Python refuses
# --------------------------------------------------------------------------
name = "Aswath"
try:
    name[0] = "B"
except TypeError as error:
    print("str error  :", error)    # 'str' object does not support item assignment

# The right way: build a NEW string
new_name = "B" + name[1:]
print(new_name)                     # Bswath
print(name)                         # Aswath  (old object is untouched)

# --------------------------------------------------------------------------
# 4. Try to change a tuple -> Python refuses
# --------------------------------------------------------------------------
point = (3, 4)
try:
    point[0] = 99
except TypeError as error:
    print("tuple error:", error)    # 'tuple' object does not support item assignment

# --------------------------------------------------------------------------
# 5. String methods also return NEW strings
# --------------------------------------------------------------------------
word = "python"
upper_word = word.upper()
print(word, upper_word)             # python PYTHON


# ==========================================================================
# PREDICT before you run!
#   t = (1, 2, 3)
#   print(t + (4,))       print(t)        print(type((5)))     print(type((5,)))
#
# TRY IT YOURSELF
#   1. Make s = "hello". Print s.replace("h", "j") and then print s.
#      Did s change?
#   2. Make frozenset({1, 2}) and try .add(3). What error do you get?
# ==========================================================================
