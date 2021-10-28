#!/usr/bin/env python
#
from itertools import islice, count, cycle, repeat, chain

for i in count(0, 10):  # <1>
    if i > 200:
        break  # <2>
    print(i, end=' ')
print("\n")

for i in islice(count(0, 10), 6):  # <3>
    print(i, end=' ')
print("\n")

giant = ['fee', 'fi', 'fo', 'fum']

for i in islice(cycle(giant), 10):  # <4>
    print(i, end=' ')
print("\n")

for i in repeat('tick', 10):  # <5>
    print(i, end=' ')

print("\n")

yn = cycle(['yes', 'no'])
# for value in yn:
#     print(value)


for word in repeat('python', 10):
    print(word)

s = "abc"
letters = ['d', 'e', 'f']
chars = 'g', 'h', 'i'


for letter in chain(s, letters, chars):
    print(letter, end=' ')
print()


