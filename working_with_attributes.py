x = [1, 2, 3]
print(type(x))
print(x.count(2))
print(x.index(3))
print(dir(x))
print(type(x.insert))

class Dog:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def bark(self):
        print("Woof! Woof!")

    @property  # uses descriptor protocol
    def age(self):  # getter property
        return self._age

    @age.setter
    def age(self, value):  # setter property
        self._age = value

    # props<tab>
    #
    # @property
    # def spam(self):
    #     return self._spam
    #
    # @spam.setter
    # def spam(self, value):
    #     pass

    # age = property(age)

    @property
    def name(self):
        return self._name

a1 = Dog('Andy', 13)
a2 = Dog('Nellie', 2)

print(dir(a1))
print(a1.name, a1.age)
print(a1.__dict__)

print(a1.name, '\n')
attribute_names = "name", "age"
for attribute_name in attribute_names:
    print(getattr(a1, attribute_name))

print(getattr(a2, "age"))

# getattr() hasattr() setattr() delattr()


print(hasattr(x, "__iter__"))
s = "abc"
print(hasattr(s, "__iter__"))
m = 5
print(hasattr(m, "__iter__"))

a1.bark()
b = getattr(a1, 'bark')
b()
getattr(a1, 'bark')()

def drool(self):
    print("drool drool drool")

setattr(Dog, 'drool', drool)

a1.drool()
a2.drool()

# delattr(Dog, 'bark')
# a1.bark()


method = "to_json"
if hasattr(a1, method):
    result = getattr(a1, method)()

if isinstance(a1, Dog):
    print("It's a Dog")

print(type(a1))
dog_type = type(a1)
a3 = dog_type("Little Bear", 2)
print(a3)
a3.bark()
print("-" * 60)

for attribute_name in dir(a1):
    if attribute_name.startswith('__'):
        continue
    attribute_value = getattr(a1, attribute_name)
    print(attribute_name, str(attribute_value)[:50])

print(__builtins__)
print(dir(__builtins__))
print(__builtins__.type(a1))
type = "Comic Sands"
type = __builtins__.type
print(type(a1))

print(dir(object))