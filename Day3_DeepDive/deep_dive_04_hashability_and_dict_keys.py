"""
==========================================================================
 Day 3 | Deep Dive 04 : Hashability - Why Only Immutables Can Be Keys
==========================================================================
 Goes deeper than Lesson 09 situation 5.

 What you will learn
   1. What hash() is and how dicts and sets use it
   2. Why mutable objects are "unhashable"
   3. A tuple is hashable ONLY if everything inside it is hashable
   4. frozenset: the hashable set

 Run this file :  python deep_dive_04_hashability_and_dict_keys.py
==========================================================================
"""

# --------------------------------------------------------------------------
# 1. hash() turns a value into a number
# --------------------------------------------------------------------------
print(hash(42))                 # 42
print(hash("a") == hash("a"))   # True -> equal values, equal hash
# A dict uses the hash to jump straight to the right "bucket", which is
# why  key in dict  is fast even with a million keys.

# --------------------------------------------------------------------------
# 2. Why a list cannot be a key
# --------------------------------------------------------------------------
# If a key could change AFTER it was stored, its hash would change and
# the dict would look in the wrong bucket - the item would be "lost".
# So Python refuses:
for candidate in [[1, 2], {1, 2}, {"a": 1}]:
    try:
        hash(candidate)
    except TypeError as error:
        print(type(candidate).__name__, "->", error)

# --------------------------------------------------------------------------
# 3. Tuples are hashable only if their contents are
# --------------------------------------------------------------------------
print(hash((1, 2)) == hash((1, 2)))     # True
try:
    hash((1, [2, 3]))
except TypeError as error:
    print("tuple with a list ->", error)  # unhashable type: 'list'

# --------------------------------------------------------------------------
# 4. frozenset can be a key or a set member
# --------------------------------------------------------------------------
friendships = {
    frozenset({"Ravi", "Sita"}): "since 2020",
}
# Order does not matter in a set, so this finds the same key:
print(friendships[frozenset({"Sita", "Ravi"})])    # since 2020

# --------------------------------------------------------------------------
# 5. The tuple puzzle: immutable outside, mutable inside
# --------------------------------------------------------------------------
t = (1, [2, 3])
t[1].append(4)          # allowed - we change the LIST, not the tuple
print(t)                # (1, [2, 3, 4])
try:
    t[1] += [5]         # list grows, THEN the tuple assignment fails!
except TypeError as error:
    print("TypeError:", error)
print(t)                # (1, [2, 3, 4, 5])  <- changed despite the error
# The tuple holds the same list object (same identity) the whole time.
# "Immutable" means the tuple's REFERENCES cannot change.


# ==========================================================================
# THINK ABOUT IT
#   Which of these can go into a set?
#     "hi"   3.5   (1, 2)   (1, [2])   frozenset({1})   None
# ==========================================================================
