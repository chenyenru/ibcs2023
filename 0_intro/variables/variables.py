# 0_intro/variables/variables.py
# Python is dynamically typed

from typing import MutableMapping
import numpy as np

# integer
myvar = 7
print(myvar)

# float
myvar = 7.3
print(myvar)

# list
# myvar = np([[2, 2], [2, 2]])
print(myvar)


myvar = """
This is a very long string
that preserves all the lines
with TRIPLE QUOTES!!!
"""


a, b = 5, 10

print(f"a:{a}\n b:{b}")

a, b = b, a
print(f"a:{a}\n b:{b}")

myvar = 20
mytype = type(myvar)
print(mytype)

myvar = "I'm a string"
mytype = type(myvar)
print(mytype)

# some  OPERATORS are overloaded
a, b = 4, 6
result = a + b
print(result)

a, b = 4, 6.7
result = a + b
print(result)

a, b = "Number", str(5)
result = a + b
print(result)


a, b = "Number", 5
# Method 1
result = a + str(b)
print(result)
# Method 2
result = f"{a}{b}"
print(result)
# <-- You can do it both way

a, b = "3", 4
result = float(a) + b
print(result)


mylist = [x for x in range(10)]
print(mylist)

mylist = list(range(0, 11, 2))
mylist = [x for x in range(0, 11, 2)]
print(mylist)


mylist = [(x * 2) for x in range(10)]
print(mylist)

filtered = [x for x in mylist if x % 2 == 0]
print(filtered)+

print((lambda x, y: x*y)(4, 2))

max_val = max(mylist)
filtered = [(max_val - x) for x in mylist if x > 5 and x < 25]
print(filtered)


# We are now slicing start:end:step
mylist = [x for x in range(50)]

sublist = mylist[1:3:2]
print(sublist)

sublist = mylist[3:15:2]
print(sublist)

sublist = mylist[3:15:-2]
print(sublist)


sublist = mylist[7:15:2]
print(sublist)

sublist = mylist[7::2]
print(sublist)

sublist = mylist[7:]
print(sublist)
