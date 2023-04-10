"""fruits = ['apple', 'banana', 'orange']
try:
    print(fruits[3])
except LookupError as e:
    print(f"Error: {e}")

string = 'x'
try:
    while True:
        string = string + string
        print(len(string))
except MemoryError:
    print('This is not funny!')

from math import exp

ex = 1

try:
    while True:
        print(exp(ex))
        ex *= 2
except OverflowError:
    print('The number is too big.')"""
