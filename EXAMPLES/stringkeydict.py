#!/usr/bin/env python


class StringKeyDict(dict):  # <1>
    def __setitem__(self, key, value):  # <2>
        if isinstance(key, str):   # <3>
            super().__setitem__(key, value)  # <4>
        else:
            raise TypeError("Keys must be strings not {}s".format(  # <5>
                type(key).__name__
            ))


if __name__ == '__main__':
    d = StringKeyDict(a=10, b=20)   # <6>
    for k, v in [('c', 30), ('d', 40), (1, 50), (('a', 1), 60), (5.6, 201)]:
        try:
            print("Setting {} to {}".format(k, v), end=' ')
            d[k] = v   # <7>
        except TypeError as err:
            print(err)  # <8>
        else:
            print('SUCCESS')

    print()
    print(d)
