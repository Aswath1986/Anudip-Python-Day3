"""
==========================================================================
 Day 3 | Lesson 10 : Your Own Objects - A First Look at Classes
==========================================================================
 The last row of the mutable table was "user class instance":
     Point(1, 2),  Dog("Rex"),  Account(balance=100)
 In this lesson we make those three ourselves.

 What you will learn
   1. class     - a blueprint for making objects
   2. __init__  - runs when a new object is made; sets its data
   3. self      - "this object"
   4. Methods   - functions that belong to the object
   5. Each object has its own value, type and identity

 Run this file :  python 10_classes_intro.py
==========================================================================
"""

# --------------------------------------------------------------------------
# 1. A Point
# --------------------------------------------------------------------------
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(1, 2)
print(p.x, p.y)            # 1 2
print(type(p))             # <class '__main__.Point'>  <- our own TYPE!

p.x = 10                   # instances are MUTABLE
print(p.x, p.y)            # 10 2

# --------------------------------------------------------------------------
# 2. A Dog with a method
# --------------------------------------------------------------------------
class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says Woof!"

rex = Dog("Rex")
tommy = Dog("Tommy")
print(rex.speak())         # Rex says Woof!
print(tommy.speak())       # Tommy says Woof!
print(rex is tommy)        # False -> two different objects

# --------------------------------------------------------------------------
# 3. An Account that changes its own value
# --------------------------------------------------------------------------
class Account:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough balance!")
        else:
            self.balance -= amount

acc = Account(balance=100)
acc.deposit(50)
acc.withdraw(500)          # Not enough balance!
acc.withdraw(30)
print("Balance:", acc.balance)   # 120

# --------------------------------------------------------------------------
# 4. Aliasing works the same way as with lists (Lesson 05)
# --------------------------------------------------------------------------
joint = acc                # second label, same account
joint.deposit(1000)
print("acc sees:", acc.balance)  # 1120


# ==========================================================================
# PREDICT before you run!
#   a = Point(0, 0)
#   b = a
#   b.y = 5
#   print(a.y)
#
# TRY IT YOURSELF
#   1. Add a method distance_from_origin() to Point that returns
#      (x**2 + y**2) ** 0.5
#   2. Make a class Student with name and a list of marks, and a method
#      average().
# ==========================================================================
