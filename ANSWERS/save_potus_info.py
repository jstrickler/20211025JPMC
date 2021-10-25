#!/usr/bin/env python
"""

@author: jstrick
Created on Wed Mar 20 23:34:17 2013

"""
import csv
import pickle
from collections import namedtuple

fields = 'term firstname lastname birthstate party'
President = namedtuple('President', fields)

presidents = []
with open('../DATA/potus.csv') as presidents_in:
    for raw_line in presidents_in:
        line = raw_line.rstrip()
        fields = line.split(',')
        president = President(*fields)
        presidents.append(president)

p = presidents[15]
print(p.firstname, p.lastname, p.party)

with open('potus.pic','wb') as POTUS:
    pickle.dump(presidents,POTUS)
