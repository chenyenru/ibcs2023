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
myvar = np([[2, 2], [2, 2]])
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
