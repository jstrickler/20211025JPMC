#!/usr/bin/env python
#
from timeit import Timer
setup = """
strings = open('../DATA/words.txt').read().splitlines()[:10000]
"""

code1 = """result = [s.upper() for s in strings]"""  # <1>
code2 = """result = list(map(str.upper, strings))"""  # <2>
t1 = Timer(code1, setup)
t2 = Timer(code2, setup)
print(t1.timeit(1000))
print(t2.timeit(1000))
