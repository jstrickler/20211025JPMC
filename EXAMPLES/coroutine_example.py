#!/usr/bin/env python


def coroutine():  # <1>
    in_value = ''
    while True:
        in_value = yield in_value.upper()  # <2>
        print('in_value:', in_value)


c = coroutine()  # <3>

print(c)  # <4>
print(next(c))  # <5>
print()

for letter in "alpha", "beta", 'gamma':
    print("out_value:", c.send(letter))  # <6>
print()


def faux_range():  # <7>
    i = 0
    while i < 4:
        yield i
        i += 1


def spam():
    yield from faux_range()  # <8>


s = spam()  # <9>

for x in s:  # <10>
    print(x)
