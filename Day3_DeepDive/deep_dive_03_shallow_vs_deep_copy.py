"""
==========================================================================
 Day 3 | Deep Dive 03 : Shallow Copy vs Deep Copy
==========================================================================
 Goes deeper than Lesson 05 section 3.

 What you will learn
   1. .copy() / list(x) / x[:] make a SHALLOW copy
   2. A shallow copy shares the INNER objects
   3. copy.deepcopy() copies everything, all the way down
   4. The [[0] * 3] * 3 grid trap

 Run this file :  python deep_dive_03_shallow_vs_deep_copy.py
==========================================================================
"""
import copy

# --------------------------------------------------------------------------
# 1. Shallow copy - new outer list, SAME inner lists
# --------------------------------------------------------------------------
original = [[1, 2], [3, 4]]
shallow = original.copy()

print(shallow is original)          # False -> outer list is new
print(shallow[0] is original[0])    # True  -> inner list is shared!

shallow[0].append(99)
print("original:", original)        # [[1, 2, 99], [3, 4]]  <- changed!

shallow.append([5])
print("original:", original)        # [[1, 2, 99], [3, 4]]  <- outer is safe

# --------------------------------------------------------------------------
# 2. Deep copy - everything is new
# --------------------------------------------------------------------------
original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)
print(deep[0] is original[0])       # False
deep[0].append(99)
print("original:", original)        # [[1, 2], [3, 4]]      <- safe

# --------------------------------------------------------------------------
# 3. Dicts behave the same way
# --------------------------------------------------------------------------
student = {"name": "Ravi", "marks": [70, 80]}
clone = student.copy()
clone["name"] = "Sita"              # replacing a value: safe
clone["marks"].append(90)           # mutating a shared list: NOT safe
print(student)                      # {'name': 'Ravi', 'marks': [70, 80, 90]}

# --------------------------------------------------------------------------
# 4. The grid trap
# --------------------------------------------------------------------------
bad_grid = [[0] * 3] * 3            # ONE inner list, referenced 3 times
bad_grid[0][0] = 1
print("bad :", bad_grid)            # [[1, 0, 0], [1, 0, 0], [1, 0, 0]]

good_grid = [[0] * 3 for _ in range(3)]    # 3 separate inner lists
good_grid[0][0] = 1
print("good:", good_grid)           # [[1, 0, 0], [0, 0, 0], [0, 0, 0]]

# Why is [0] * 3 fine? Because 0 is IMMUTABLE - sharing it is harmless.


# ==========================================================================
# THINK ABOUT IT
#   Does a tuple of ints ever need a deep copy? Why or why not?
# ==========================================================================
