"""
==========================================================================
 Day 3 | Lesson 08 : Identity, Membership and Logical Operators
==========================================================================
 What you will learn
   1. Identity operators    is   is not
   2. Membership operators  in   not in
   3. Logical operators     and  or  not   (previewed in Day 2 Lesson 08)
   4. Quick revision: bin() and hex()

 Run this file :  python 08_identity_membership_logical_operators.py
==========================================================================
"""

# --------------------------------------------------------------------------
# 1. Identity operators - are these the SAME object?
# --------------------------------------------------------------------------
x = 5
y = x
print(x == y)          # True   -> equal values
print(x is y)          # True   -> same object
print(x is not y)      # False

value = None
print(value is None)   # True   -> the correct way to check for None

# --------------------------------------------------------------------------
# 2. Membership operators - is it inside?
# --------------------------------------------------------------------------
print("Aswath and s present or not ? :", "swa" in "Aswath")   # True
print("z" not in "Aswath")              # True

fruits = ["apple", "mango"]
print("mango" in fruits)                # True
print("grape" in fruits)                # False

marks = {"ravi": 80, "sita": 92}
print("ravi" in marks)                  # True  -> checks the KEYS of a dict
print(80 in marks)                      # False -> values are not checked

# --------------------------------------------------------------------------
# 3. Logical operators
# --------------------------------------------------------------------------
#   and -> True only if BOTH sides are True
#   or  -> True if AT LEAST ONE side is True
#   not -> flips True <-> False
age = 20
has_id = True
print(age >= 18 and has_id)     # True
print(age < 18 or has_id)       # True
print(not has_id)               # False

# and / or return one of the OBJECTS, not always True/False
print("" or "Guest")            # Guest  -> "" is falsy, so the right side
print("Ravi" or "Guest")        # Ravi   -> first truthy value wins
print(0 and 10)                 # 0      -> stops at the first falsy value

# --------------------------------------------------------------------------
# 4. Revision from class: bin() and hex()
# --------------------------------------------------------------------------
print(bin(5))          # 0b101
print(hex(10))         # 0xa


# ==========================================================================
# PREDICT before you run!
#   print("a" in "Anudip")       print("A" in "Anudip")
#   print(3 in (1, 2, 3))        print(not [])
#
# TRY IT YOURSELF
#   1. Ask for a username. Use "or" to use "Guest" if it is empty.
#   2. Ask for a letter and print whether it is a vowel using:
#        letter in "aeiouAEIOU"
# ==========================================================================
