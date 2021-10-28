#!/usr/bin/python
import bs4

with open('../DATA/people.xml') as people_in:  # <1>
    soup = bs4.BeautifulSoup(people_in, 'lxml')  # <2>

new_tag = soup.new_tag('person', org='Oracle')  # <3>
new_tag.string = 'Larry Ellison'  # <4>

people = soup.find('people')  # <5>
people.append(new_tag)  # <6>

suite_tag = soup.find('suite')  # <7>
suite_tag.decompose()   # <8>

new_xml = soup.prettify()  # <9>
print(new_xml)
