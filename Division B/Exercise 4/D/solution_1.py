# Python 3.12.1

partys = []
sumcnt = 0
i = 0

with open('C:/python/yandex_algo_trainee_v2/input.txt', 'rt', encoding = 'utf-8') as file_input:
    for line in file_input:
        words = line.split()
        cnt = int(words[-1])
        partyname = ' '.join(words[:-1])
        partys.append([partyname, cnt, i])
        sumcnt += cnt
        i += 1

f = sumcnt / 450
free = 450

for i in range(len(partys)):
    party = partys[i]
    party.append(party[1] // f)
    free -= party[1] // f
    party.append(party[1] % f)

partys.sort(key = lambda x: x[4], reverse = True)
for i in range(int(free)):
    partys[i][3] += 1
partys.sort(key = lambda x: x[2])
for party in partys:
    print(party[0], int(party[3]))
