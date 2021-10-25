from collections import defaultdict

counts = defaultdict(list)   # provide function that returns default value

with open('DATA/words.txt') as words_in:
    for raw_word in words_in:
        word = raw_word.rstrip()
        if len(word) < 4:
            first_letter = word[0]
            # if first_letter not in counts:
            #     counts[first_letter] = []
            counts[first_letter].append(word)

for letter, words in counts.items():
    print(letter, words)
print()

def zero():
    return 0

colors = defaultdict(zero)   # colors = defaultdict(lambda: 0)
colors['red'] = 5
colors['purple'] = 10
colors['pink'] = 28
colors['green'] = 15
print(colors)
for color in 'red green blue orange yellow pink black white'.split():
    print(color, colors[color])


capitals = {'TX': 'Austin', 'NC': 'Raleigh', 'NJ': 'Trenton'}
print(capitals.get('CA'))
print(capitals.get('CA', 'Not defined'))


