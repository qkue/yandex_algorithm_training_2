# Python 3.12.1

votes = dict()

with open('input.txt', 'rt', encoding = 'utf-8') as file_input:
    for line in file_input.readlines():
        last_name, number = line.rstrip().split()
        if last_name not in votes:
            votes[last_name] = 0
        votes[last_name] += int(number)

answer = []
for last_name in sorted(votes):
    answer.append(last_name + ' ' + str(votes[last_name]))

print('\n'.join(answer))
