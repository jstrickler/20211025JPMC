from datetime import date

dates = [
    (1968, 10, 11),
    (1968, 12, 21),
    (1969, 3, 3),
    (1969, 5, 18),
    (1969, 7, 16),
    (1969, 11, 14),
    (1970, 4, 11),
    (1971, 1, 31),
    (1971, 7, 26),
    (1972, 4, 16),
    (1927, 12, 7),
]  # <1>

all_dates = []
for dt in dates:
    d = date(*dt)  # <2>
    all_dates.append(d)

print(all_dates)
# d = (1971, 1, 31)
#  Date(d)


print()

fruits = ["pomegranate", "cherry", "apricot", "date", "Apple", "lemon", "Kiwi",
          "ORANGE", "lime", "Watermelon", "guava", "papaya", "FIG", "pear",
          "banana", "Tamarind", "persimmon", "elderberry", "peach", "BLUEberry",
          "lychee", "grape"]

sort_opts = {
    'key': lambda e: e.lower(),
    'reverse': True,
#    "wombat": 25,
}  # <3>

sorted_fruits = sorted(fruits, **sort_opts)  # <4>
print(sorted_fruits)

def addem(a, b):
    return a + b

print(addem(10, 20))
print(addem(1, 9))
values = 42, 58
print(addem(*values))   # addem(values[0], values[1])

person = 'Bill', 'Gates', 'Microsoft', '1955-10-25'
first_name, last_name, product, dob = person
#  first_name = person[0]
#  last_name = person[1]
# ...
x = [1, 2, 3,]
print(x)
t = 5,
print(t, type(t))

values = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
x, y, *z = values
print(x, y, z)

x, *y, z = values
print(x, y, z)

*x, y, z = values
print(x, y, z)

data = [
    ('John', 'Strickler', 'VA', 'NC', 'DC'),
    ('Fred', 'Smith', 'WI'),
    ('Srini', 'Srinivasan'),
    ('Mary', 'Rodriguez', 'NM'),
]
for first_name, last_name, *state in data:
    print(first_name, last_name, state)




