#!/usr/bin/env python
#
import unicodedata as u

shalom = u'\u05e9\u05dc\u05d5\u05dd'

print(shalom, '\n')

for c in shalom:
    print(u.name(c))
