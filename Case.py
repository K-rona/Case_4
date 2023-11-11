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

    next_word = np.random.choice(dictionary[first_word[-1]])
    result.append(next_word)

    for i in symbols:
        if i in next_word:
            count += 1

print(' '.join(result))
