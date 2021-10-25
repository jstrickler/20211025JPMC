#!/usr/bin/env python
"""

@author: jstrick
Created on Wed Mar 13 20:45:42 2013

"""
from collections import defaultdict

dd = defaultdict(lambda: 0)  # <1>

dd['spam'] = 10  # <2>
dd['eggs'] = 22

print(dd['spam'])  # <3>
print(dd['eggs'])
print(dd['foo'])  # <4>

print('-' * 60)

fruits = ["pomegranate", "cherry", "apricot", "date", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape" ]

fruit_info = defaultdict(list)

for fruit in fruits:
    first_letter = fruit[0]
    fruit_info[first_letter].append(fruit)

for letter, fruits in sorted(fruit_info.items()):
    print(letter, fruits)

