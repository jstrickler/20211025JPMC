#!/usr/bin/env python


class MultiIndexList(list):  # <1>

    def __getitem__(self, item):  # <2>
        if isinstance(item, tuple):  # <3>
            if len(item) == 0:
                raise ValueError("Tuple must be non-empty")
            else:
                tmp_list = []
                for index in item:
                    tmp_list.append(
                        super().__getitem__(index)  # <4>
                    )
                return tmp_list
        else:
            return super().__getitem__(item)  # <5>


if __name__ == '__main__':
    m = MultiIndexList(
        'banana peach nectarine fig kiwi lemon lime'.split()
    )  # <6>
    m.append('apple')  # <7>
    m.append('mango')
    print(m)

    print(m[0])
    print(m[1])
    print(m[5, 2, 0])  # <8>
    print(m[:4])
    print(len(m))
    print(m[5, ])
    print(m[:2, -2:])
    print()
    print(m)
    m.extend(['durian', 'kumquat'])
    print(m)
    print()
    for fruit in m:
        print(fruit)
    print(len(fruit))
