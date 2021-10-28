import operator as op
from functools import partial

def hello():
    print("HELLO")

def doit(some_function):
    some_function()  # not some_function

doit(hello)  # not doit(hello())

doit(lambda: print("WHOOHOOO"))

#  lambda params....: return value

def tri_func(x, y, z):
    print("params:", x, y, z)
    return ((x * 10) + y) * z

tf = partial(tri_func, 25)

def compute(a, b, some_function):
    return some_function(a, b)  # calling the callback

print("partial:", compute(5, 10, tf))

def my_op(i, j):
    return 42

print(compute(5, 10, lambda x, y: x + y))
print(compute("abc", "def", lambda x, y: x + ',' + y))
print(compute(5, 10, op.add))
print(compute(2, 5, op.pow))
print(compute(1000, "wombat", my_op))
m = [1, 2, 3, 2, 4, 2, 9]
print(m.count(2))

print(op.countOf(m, 2))


fruits = ["pomegranate", "cherry", "apricot", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE", "date"]

print(sorted(fruits), '\n')

def ignore_case(s):
    return s.lower()

# sort strings, ignoring case
print(sorted(fruits, key=ignore_case), '\n')
print(sorted(fruits, key=lambda s: s.lower()), '\n')
print(sorted(fruits, key=str.lower), '\n')

# universal function
def foo(*args, **kwargs):   # keyword args
    print(args)
    print(kwargs)

foo(1)
foo(1, 2, 3, 4, 5)
foo(name="Fred", animal="wombat")
foo(1, 2, name="Bob", animal="Wildebeest")
foo()

def myfunc(x, *, file_name, repeat_count):
    print("myfunc:", x, file_name, repeat_count)

myfunc(25, file_name="foo.txt", repeat_count=4)

pf = partial(myfunc, repeat_count=5)

pf(100, file_name="spam.txt")

def doit(func):
    func(10, file_name="toast.txt")

doit(pf)



