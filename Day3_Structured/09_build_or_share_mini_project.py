"""
==========================================================================
 Day 3 | Lesson 09 : Mini Project - Build or Share?
==========================================================================
 This is Section 4 of the "Mutability Lab" page.
 Motto:   BUILD with mutable  ·  SHARE as immutable

 Work through it with the PRIMM method:
   P - PREDICT     : read the code, guess each print
   R - RUN         : run it and compare
   I - INVESTIGATE : change one thing at a time
   M - MODIFY      : add one more situation of your own
   M - MAKE        : see the bottom of the file

 Run this file :  python 09_build_or_share_mini_project.py
==========================================================================
"""

# --------------------------------------------------------------------------
# Situation 1 - A shopping cart that grows   -> BUILD it (list)
# --------------------------------------------------------------------------
cart = []
cart.append("pen")
cart.append("notebook")
print("Cart:", cart)

# --------------------------------------------------------------------------
# Situation 2 - GPS position of a shop        -> SHARE it (tuple)
# --------------------------------------------------------------------------
# It should never change by accident, so we use a tuple.
SHOP_LOCATION = (13.0827, 80.2707)
print("Shop at:", SHOP_LOCATION)

# --------------------------------------------------------------------------
# Situation 3 - Days of the week              -> SHARE it (tuple)
# --------------------------------------------------------------------------
WEEK_DAYS = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")

# --------------------------------------------------------------------------
# Situation 4 - Marks being entered           -> BUILD it (dict)
# --------------------------------------------------------------------------
marks = {}
marks["ravi"] = 78
marks["sita"] = 91
marks["ravi"] += 2           # correction
print("Marks:", marks)

# --------------------------------------------------------------------------
# Situation 5 - Using something as a dict KEY -> must be IMMUTABLE
# --------------------------------------------------------------------------
# Immutable objects are "hashable", so they can be keys.
distance = {}
distance[("Chennai", "Pune")] = 1185     # tuple key: OK
print("Distance:", distance)

try:
    distance[["Chennai", "Delhi"]] = 2180   # list key: NOT allowed
except TypeError as error:
    print("List as key ->", error)          # unhashable type: 'list'

# --------------------------------------------------------------------------
# Situation 6 - Builder pattern: build mutable, then freeze it
# --------------------------------------------------------------------------
letters = []
for ch in "banana":
    if ch not in letters:
        letters.append(ch)        # build with a list
final_letters = tuple(letters)    # then share as a tuple
print("Unique letters:", final_letters)    # ('b', 'a', 'n')


# ==========================================================================
# PREDICT before you run!
#   Which of these can be a dict key?
#     5      "abc"      (1, 2)      [1, 2]      {1, 2}      frozenset({1, 2})
#
# MAKE - your own program
#   Make a "class attendance" program:
#     - BUILD a list of present students using input() in a while loop
#       (stop when the user types "done")
#     - at the end, convert it to a tuple and print it with its length
# ==========================================================================
