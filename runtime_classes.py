
class Animal:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

class Cat(Animal):
    def __init__(self, breed, age):
        super().__init__(age)
        self.breed = breed

    @property
    def breed(self):  # getter property
        if isinstance(breed, str):
            return self._breed
        else:
            raise TypeError("Breed must be a string")

c1 = Cat('Tabby', 14)
c2 = Cat('Persian', 2)
print(c1, c2)
print(c1.age, c1.breed)  # not c1.breed() or c1.get_breed()
print(c1.breed)
c1.breed = "Manx"
def __init__(wombat, breed, age):
    Animal.__init__(wombat, age)
    wombat._breed = breed

@property
def breed(self):
    return self._breed

Dog = type('Dog', (Animal,), {'__init__': __init__,
                              'breed': breed})

d1 = Dog("English Shepherd", 2)
d2 = Dog("Mutt", 14)
print(d1, d2)
print(d1.breed)
print(d2.age)