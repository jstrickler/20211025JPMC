from random import randint
from uuid import uuid4

def random_int_generator(max_values):
    for i in range(max_values):
        yield randint(1, 1000)
        # print("wombat!")

r  = random_int_generator(10)
for i in r:
    print(i)  # next(r)
print("Again:")
for i in r:
    print(i)

def id_generator():
    while True:
        yield uuid4()

idg = id_generator()
print(idg)
print(next(idg))
print(next(idg))
print(next(idg))

names = ['Lakshmi', 'Srini', 'Bernardo']
for name in names:
    print(name, next(idg))


