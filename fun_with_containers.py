from random import randint

class WeirdContainer:

    def __getitem__(self, index):
        return 42

    def __delitem__(self, index):
        print("HA HA you can't delete!!")

    def __len__(self):
        return randint(1, 1000)

    def __str__(self):
        return "I am so pretty"

x = WeirdContainer()

print(x[5])
print(x['wombat'])
del x[75]
for i in range(10):
    print(len(x))
print(x)


class RoundingDict(dict):
    def __init__(self, *args, num_places=3):
        super().__init__(*args)
        self._num_places = num_places

    def __setitem__(self, key, value):
        super().__setitem__(key, round(value, self._num_places))

rd1 = RoundingDict(num_places=1)
rd1['a'] = 3.398239029323
rd1['b'] = 4.3912930239
print(rd1)