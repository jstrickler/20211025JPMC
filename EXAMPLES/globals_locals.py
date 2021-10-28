#!/usr/bin/env python
from pprint import pprint  # <1>

spam = 42
ham = 'Smithfield'






def eggs(fruit):  # <3>
    def bacon():
        pass
    name = 'Lancelot'  # <4>
    idiom = 'swashbuckling'  # <4>
    print("Globals:")
    pprint(globals())  # <5>
    print()
    print("Locals:")
    pprint(locals())  # <6>


eggs('mango')

g = globals()
print(g.get('ham'))
print(g['ham'])

g['color'] = 'blue'
print(color)

g['bark'] = lambda : print("woof! woof!")

print(dir(g))





bark()

# del g['color']   #  del color
# print(color)




