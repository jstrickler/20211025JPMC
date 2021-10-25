from collections import Counter

with open('DATA/words.txt') as words_in:
    first_letters = [word[0] for word in words_in]

word_counts = Counter(first_letters)
print(word_counts)

c = Counter()
c['ham'] += 1
c['spam'] += 1
c['ham'] += 1
print(c)

x = [
    'spam', 'spam', 'spam', 'spam', 'spam', 'spam',
'spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'spam',
'spam', 'spam', 'spam', 'spam', 'eggs', 'spam',
]
print(Counter(x))
