"""
==========================================================================
 Day 3 | Lesson 01 : What is a Python Object?
==========================================================================
 What you will learn
   1. Every value in Python is an OBJECT
   2. Every object has three things : VALUE, TYPE, IDENTITY
   3. A variable is only a NAME (a label) that points to an object
   4. type() and id() let us look at an object

 Run this file :  python 01_what_is_an_object.py
==========================================================================
"""

# --------------------------------------------------------------------------
# 1. The four words from the class slide
# --------------------------------------------------------------------------
#   Word            Question it answers               How to see it
#   Value           What does it hold?                print(x)
#   Type            What kind of object is it?        type(x)
#   Identity        Where does the object live?       id(x)
#   Label / Name    Which label points to it?         the variable name, x
#
#   The NAME is not the object. The name is a sticky note on the box.

x = 42

print("Value    :", x)          # 42
print("Type     :", type(x))    # <class 'int'>
print("Identity :", id(x))      # a big number - different on every computer

# --------------------------------------------------------------------------
# 2. Different values, different types
# --------------------------------------------------------------------------
print(type(3.14))       # <class 'float'>
print(type("hello"))    # <class 'str'>
print(type(True))       # <class 'bool'>
print(type([1, 2, 3]))  # <class 'list'>
print(type(None))       # <class 'NoneType'>

# --------------------------------------------------------------------------
# 3. A name is a label - we can move it to another object
# --------------------------------------------------------------------------
x = 42
print("x ->", x, "id:", id(x))

x = "now I am text"      # the label x moves to a NEW object
print("x ->", x, "id:", id(x))   # different id, different type

# The old object 42 did not change. Only the label moved.

# --------------------------------------------------------------------------
# 4. Two labels on the same object
# --------------------------------------------------------------------------
a = [10, 20]
b = a                    # b is a second label on the SAME list
print(id(a) == id(b))    # True -> same identity, same object


# ==========================================================================
# PREDICT before you run!
#   print(type(10 / 2))        print(type("5"))        print(type(5 > 3))
#
# TRY IT YOURSELF
#   1. Make a variable city = "Chennai". Print its value, type and id.
#   2. Now write city = "Pune". Print the id again. Did it change? Why?
# ==========================================================================
