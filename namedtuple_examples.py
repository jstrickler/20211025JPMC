from collections import namedtuple

place = 'St. Louis', 'MO'
print(place[0], place[1])
city, state = place   # interable unpacking

Place = namedtuple('Place', 'city state')
Place = namedtuple('Place', ['city', 'state'])

place = Place('St. Louis', 'MO')

print(place[0], place[1])
print(place.city, place.state)
print(type(place))

p2 = place._replace(city='Kansas City')
print(place)
print(p2)

d = place._asdict()
print(d)

print(place._fields)





