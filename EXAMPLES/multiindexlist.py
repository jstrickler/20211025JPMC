#!/usr/bin/env python


class MultiIndexList(list):  # <1>
    """
    List which accepts a tuple of integers as an index

    foo[0] or foo[1, 2, 3]
    """
    #     foo[indexes]     either foo[5] or foo[5, 6, 3]   :: bad tuple: foo[]
    def __getitem__(self, indexes):  # <2>
        if isinstance(indexes, tuple):  # <3>
            if len(indexes) == 0:
                raise ValueError("Tuple must be non-empty")
            else:
                tmp_list = []
                for index in indexes:
                    tmp_list.append(
                        super().__getitem__(index)  # <4>
                    )
                return tmp_list
        else:
            return super().__getitem__(indexes)  # <5>

    #  foo[index] = value
    def __setitem__(self, index, value):
        super().__setitem__(int(index), value)



if __name__ == '__main__':
    m = MultiIndexList(
        'banana peach nectarine fig kiwi lemon lime'.split()
    )  # <6>
    m.append('apple')  # <7>
    m.append('mango')
    print(m)

    print(m[0])
    print(m[1])
    print("multi-index:", m[5, 2, 0])  # <8>
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

    stupid_tuple = ()  # empty tuple

    try:
        print(m[stupid_tuple])
    except Exception as err:
        print(err)

    smart_tuple = 5, 1, 2
    print(m[smart_tuple])

#    print(m['spam'])


    m[1.2] = "cherry"
    m["3"] = "grapefruit"

    print(m)