from random import *
import numpy as np

'''
with open("input.txt", "r", encoding='utf8') as f_in:
    text = f_in.read().split()

number = int(text[0])
text = text[1:]
dictionary = {}
words = []

for i in range(len(text)):

    if text[i] in dictionary:

        dictionary[text[i]] += [text[i + 1]]

    else:
        dictionary[text[i]] = []
        words += [text[i]]

count = 0
result = []
symbols = ".?!"

while count <= number:

    first_word = np.random.choice(words)
    result.append(first_word)
    result.append(np.random.choice(dictionary[first_word]))

print(" ".join(result))
'''

'''with open('input.txt', 'r', encoding='utf8') as f_in:
    number = f_in.readline()
    text = f_in.read()

corpus = text.split()


def make_pairs(corpus):
    for i in range(len(corpus) - 1):
        return corpus[i], corpus[i + 1]


pairs = make_pairs(corpus)
print(pairs)
word_dict = {}

for word_1, word_2 in pairs:
    if word_1 in word_dict.keys():
        word_dict[word_1].append(word_2)
    else:
        word_dict[word_1] = [word_2]

symbols = ".?!"
count = 0
first_word = np.random.choice(corpus)
chain = []

while count <= number:
    first_word = np.random.choice(corpus)

    for i in symbols:
        if i in first_word:
            count += 1

    chain += [first_word]
    chain.append(np.random.choice(word_dict[chain[-1]]))

print(' '.join(chain))
'''

with open('input.txt', 'r', encoding='utf-8') as f_in:
    number = int(f_in.readline().rstrip())
    text = f_in.read()

words = text.split()

symbols = ".?!"
count = 0
dictionary = {}

for i in range(len(words)):

    if words[i] in dictionary:
        dictionary[words[i]].append(words[i+1])

    else:
        dictionary[words[i]] = []

first_word = np.random.choice(words)
for i in symbols:
    if i in first_word:
        count += 1

result = [first_word]

while count <= number:

    next_word = np.random.choice(dictionary[first_word])
    result.append(next_word)

    for i in symbols:
        if i in next_word:
            count += 1

print(' '.join(result))
