#!/usr/bin/env python
from sys import getsizeof
from array import array
import numpy as np
from random import randint

values = [randint(1, 30000) for i in range(1000000)]  # <1>

print(f'Size of integer list: {getsizeof(values)}\n')

nparray = np.array(values)
print(f'Size of numpy array: {getsizeof(nparray)}  Contents:',
      nparray[:5], '...')  # <3>

for datatype in 'i', 'h', 'L', 'Q', 'd':
    data_array = array(datatype, values)  # <2>
    print(f'Size of {datatype} array: {getsizeof(data_array)}  Contents:',
          data_array[:5], '...')  # <3>
    print()
