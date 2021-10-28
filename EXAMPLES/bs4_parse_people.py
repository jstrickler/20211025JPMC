#!/usr/bin/python
import bs4

with open('../DATA/people.xml') as people_in:
    soup = bs4.BeautifulSoup(people_in, 'lxml')
    
for person in soup.findAll('person'):
    print("{0}, {1}".format(person.string, person.get('org')))
