"""
==========================================================================
 Day 3 | Lesson 03 : Mutable Types (can be changed in place)
==========================================================================
 What you will learn
   1. What "mutable" means
   2. The mutable types: list, dict, set, bytearray, deque, array,
      and objects made from your own class
   3. The identity (id) stays the SAME while the value changes

 Run this file :  python 03_mutable_types.py
==========================================================================
"""
from collections import deque
from array import array

# --------------------------------------------------------------------------
# 1. Mutable = the SAME object can change its value.
# --------------------------------------------------------------------------

# list
marks = [1, 2, 3]
before = id(marks)
marks.append(4)
marks[0] = 100
print("list      :", marks, "same object?", id(marks) == before)   # True

# dict
person = {"name": "Ana", "age": 30}
person["age"] = 31
person["city"] = "Delhi"
print("dict      :", person)

# set
colours = {"red", "blue"}
colours.add("green")
colours.discard("red")
print("set       :", sorted(colours))      # sorted only to print in order

# bytearray - a mutable version of bytes
data = bytearray(b"hi")
data[0] = 72                                # 72 is the code for 'H'
print("bytearray :", data)                  # bytearray(b'Hi')

# deque - a list that is fast at BOTH ends
queue = deque([1, 2, 3])
queue.appendleft(0)
queue.append(4)
print("deque     :", queue)                 # deque([0, 1, 2, 3, 4])

# array - a list where every item has the same type ("i" = int)
numbers = array("i", [1, 2, 3])
numbers[1] = 20
print("array     :", numbers)               # array('i', [1, 20, 3])

# --------------------------------------------------------------------------
# 2. Objects from your own class are mutable too
# --------------------------------------------------------------------------
class Account:
    def __init__(self, balance):
        self.balance = balance

acc = Account(balance=100)
before = id(acc)
acc.balance = acc.balance + 50
print("Account   :", acc.balance, "same object?", id(acc) == before)  # 150 True

# --------------------------------------------------------------------------
# 3. Summary table (from class)
# --------------------------------------------------------------------------
#   IMMUTABLE                          MUTABLE
#   int, float, bool, complex          list
#   str, bytes                         dict
#   tuple, frozenset                   set
#   range, None                        bytearray, deque, array
#                                      your own class instances


# ==========================================================================
# PREDICT before you run!
#   s = {1, 2}
#   s.add(2)
#   print(s)          print(len(s))
#
# TRY IT YOURSELF
#   1. Make a dict of 3 students and their marks. Increase one mark by 5.
#      Print id() before and after. Is it the same object?
#   2. Make a class Dog with a name. Create Dog("Rex"), then change its name.
# ==========================================================================
