from copy import deepcopy

data = ['alpha', 'beta', 'gamma']
#  list data = new list(...);
# binds 'data' to list object
spam = data   # another name (alias) for same object
print(spam is data)
print(id(spam) == id(data))
data.append('delta')
print("data:", data)
print("spam:", spam)
del data
print("spam after del:", spam)
ham = list(spam)  # distinct object
print(spam is ham)
spam.append('epsilon')
print("spam:", spam)
print("ham:", ham)
junk = [1, 2, 3]
spam.append(junk)
print("spam:", spam)
toast = list(spam)  # SHALLOW copy
print("toast:", toast)
print(spam is toast, id(spam), id(toast))
spam[-1].append(99)
print("spam:", spam)
print("toast:", toast)
jam = deepcopy(spam)  # DEEP (recursive) copy
spam[-1].append(42)
print("spam:", spam)
print("jam:", jam)
butter = spam.copy()  # SHALLOW copy
print("butter:", butter)
butter[-1].append(1000)
print("spam:", spam)
print("butter:", butter)

colors = ['purple', 'yellow', 'orange']

def foo(data):
    local_data = deepcopy(data)
    local_data.append('red')

foo(colors)
print(colors)

import typing as T

x: T.List[T.Dict[str, int]] = [
    {'blah': 5},
    {'foo': [1, 2, 3]},
    {'bar': {'a': 5}},
#     ['spam', 'ham'],
]


print(type(x))
print(type(x[0]))
