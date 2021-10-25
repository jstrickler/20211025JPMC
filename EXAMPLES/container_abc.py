#!/usr/bin/env python
from collections.abc import Sized, Iterator  # <1>


class BadContainer(Sized):  # <2>
    pass


class GoodContainer(Sized):
    def __len__(self):   # <3>
        return 42


try:
    bad = BadContainer()  # <4>
except TypeError as err:
    print(err)  # <5>
else:
    print(bad)

print()

try:
    good = GoodContainer()  # <6>
except TypeError as err:
    print(err)
else:
    print(good)  # <7>
    print(len(good))  # <8>

print()


class MyIterator(Iterator):  # <9>
    data = 'a', 'b', 'c'
    index = 0

    def __next__(self):  # <10>
        if self.index >= len(self.data):
            raise StopIteration
        else:
            return_val = self.data[self.index]
            self.index += 1
            return return_val


m = MyIterator()  # <11>
for i in m:  # <12>
    print(i)
print()

print(hasattr(m, '__iter__'))  # <12>
