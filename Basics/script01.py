# import this
import csv
import sys
from typing import List

print(sys.platform)
print(2 ** 100)

x = 'Spam!'
print(x * 8)


# Lists
def square(x):
    return x ** 2


L = [1, 2, 3]
print(list(map(square, L)))

# Dictionaries
dict = {'k': 'v'}
dict['l'] = 3
dict['l'] = 4
print(dict)


def count_up_to(max):
    count = 1
    while count <= max:
        if count % 2 == 0:
            yield count
        count += 1


counter = count_up_to(5)
for num in counter:
    print(num)

print(repr(counter))


