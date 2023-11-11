with open('input.txt', 'r', encoding='utf-8') as f_in:
    number = int(f_in.readline().rstrip())
    text = f_in.read()

words = text.split()

symbols = ".?!"
count = 0
dictionary = {}

for word1 in range(len(words) - 1):
    word2 = word1 + 1

    if words[word1] in dictionary.keys():
        dictionary[words[word1]].append(words[word2])
    else:
        dictionary[words[word1]] = [words[word2]]

words.pop(len(words) - 1)
print(dictionary)

first_word = np.random.choice(words)

for i in symbols:
    if i in first_word:
        count += 1

result = [first_word]

while count <= number:

    next_word = np.random.choice(dictionary[result[-1]])
    result.append(next_word)

    for i in symbols:
        if i in next_word:
            count += 1

print(' '.join(result))
