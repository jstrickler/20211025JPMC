
with open('DATA/mary.txt') as mary_in:
    print(mary_in)
    print(hasattr(mary_in, '__iter__'))
    for line in mary_in:  # mary_in is a generator (also an iterator)
        print(line.rstrip())
print('-' * 60)

with open('DATA/mary.txt') as mary_in:
    print(next(mary_in))
    print(next(mary_in))
    for line in mary_in:
        # line = next(mary_in)
        print(line.rstrip())

foo = ['a', 'b', 'c']
for c in foo:
    print(c)
print()
# print(next(foo))
ifoo = iter(foo)  # get the iterator from an iterable
print(next(ifoo))
print(next(ifoo))
print(next(ifoo))
print(hasattr(foo, '__iter__'))
print(hasattr(foo, '__next__'))
print(hasattr(ifoo, '__next__'))
print(hasattr(mary_in, '__iter__'))
print(hasattr(mary_in, '__next__'))

