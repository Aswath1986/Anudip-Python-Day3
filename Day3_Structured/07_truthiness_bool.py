"""
==========================================================================
 Day 3 | Lesson 07 : Truthiness - bool() of Any Object
==========================================================================
 What you will learn
   1. Every object can be turned into True or False with bool()
   2. "Empty" or "zero" things are False. Everything else is True
   3. Using truthiness in an if statement

 Run this file :  python 07_truthiness_bool.py
==========================================================================
"""

# --------------------------------------------------------------------------
# 1. From the class code
# --------------------------------------------------------------------------
print(bool(0))        # False
print(bool([]))       # False  (empty list)
print(bool(""))       # False  (empty string)
print(bool(None))     # False

# --------------------------------------------------------------------------
# 2. The full list of "falsy" values
# --------------------------------------------------------------------------
#   0   0.0   0j   ""   []   ()   {}   set()   range(0)   None   False
falsy = [0, 0.0, 0j, "", [], (), {}, set(), range(0), None, False]
for value in falsy:
    print(repr(value), "->", bool(value))

# --------------------------------------------------------------------------
# 3. Everything else is "truthy" - even these!
# --------------------------------------------------------------------------
print(bool(-1))       # True   (any non-zero number)
print(bool(" "))      # True   (a space is a character)
print(bool("False"))  # True   (a non-empty string)
print(bool([0]))      # True   (a list with one item)

# --------------------------------------------------------------------------
# 4. Using it in if
# --------------------------------------------------------------------------
cart = []
if cart:
    print("Proceed to payment")
else:
    print("Your cart is empty")      # this one prints

name = "Aswath"
if name:
    print("Hello,", name)


# ==========================================================================
# PREDICT before you run!
#   print(bool(0.0001))    print(bool("0"))    print(bool({}))   print(bool((0,)))
#
# TRY IT YOURSELF
#   Ask the user for their name with input(). If they press Enter without
#   typing anything, print "Name cannot be empty".
# ==========================================================================
