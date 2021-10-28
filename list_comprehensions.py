fruits = ['apple', 'banana', 'mango', 'kiwi', 'pomegranate']

f0 = []
for f in fruits:
    f0.append(f.upper())
print("f0:", f0)

f1 = [f.upper() for f in fruits]
# result_list = [EXPR for VAR in ITERABLE if CONDITION]
print("f1:", f1)

f2 = [f.upper() for f in fruits if len(f) > 5]
print("f2:", f2)
print(" ".join(f2))
print("/".join(f2))

airports = {
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'YCC': 'Calgary',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'YOW': 'Ottawa',
    'IAD': 'Dulles',
}

d = {k.lower(): v.upper() for k, v in airports.items()}
print(d)

d = {f[0].upper(): f for f in fruits}
print(d)

food = ['Spam', 'spam', 'SPAM', 'eggs', 'Eggs', 'EGGS', 'EGGS',
        'spaM', 'spam', 'spam']

f1 = {f.lower() for f in food}
print(f1)

print(fruits, '\n')
g1 = (f.upper() for f in fruits)  # generator expression
print(g1)
for fruit in g1:
    print(fruit)
print()
print("second try:")
for fruit in g1:
    print(fruit)

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

dobs = (p[3] for p in people)
print(dobs)
for dob in dobs:
    print(dob)




