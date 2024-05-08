# Python 3.12.1

words = dict()

with open('input.txt', 'rt', encoding = 'utf-8') as file_input:
    for word in file_input.read().split():
        #word = line.rstrip()
        if word not in words:
            words[word] = 0
        words[word] += 1

sorted_words = []
for key, value in words.items():
    sorted_words.append((value, key))
sorted_words.sort(key = lambda x: (-x[0], x[1]))

answer = []
for word in sorted_words:
    answer.append(word[1])

print('\n'.join(answer))
