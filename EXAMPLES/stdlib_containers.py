#!/usr/bin/env python
from collections import Counter, defaultdict, deque, namedtuple, OrderedDict

# Counter
with open('../DATA/words.txt') as words_in:
    all_words = [line[0] for line in words_in]
    word_counter = Counter(all_words)  # <1>


print(word_counter.most_common(10))  # <2>
print('-' * 60)

# defaultdict
fruits = ["pomegranate", "cherry", "apricot", "date", "apple",
          "lemon", "kiwi", "orange", "lime", "watermelon", "guava",
          "papaya", "fig", "pear", "banana", "tamarind", "persimmon",
          "elderberry", "peach", "blueberry", "lychee", "grape"]

fruit_by_first = defaultdict(list)  # <3>

for fruit in fruits:
    fruit_by_first[fruit[0]].append(fruit)  # <4>

for letter, fruits in sorted(fruit_by_first.items()):
    print(letter, fruits)
print('-' * 60)

# deque
d = deque()  # <5>
for c in 'abcdef':
    d.append(c)   # <6>
print(d)
for c in 'ghijkl':
    d.appendleft(c)  # <7>
print(d)
d.extend('mno')  # <8>
print(d)
d.extendleft('pqr')  # <9>
print(d)
print(d[9])
print(d.pop(), d.popleft())  # <10>
print(d)
print('-' * 60)


# namedtuple
President = namedtuple('President', 'first_name, last_name, party')  # <11>
p = President('Theodore', 'Roosevelt', 'Republican')  # <12>
print(p, len(p))
print(p[0], p[1], p[-1])
print(p.first_name, p.last_name, p.party)  # <13>

p = President(last_name='Lincoln', party='Republican', first_name='Abraham')
print(p)
print(p.first_name, p.last_name)
print('-' * 60)

