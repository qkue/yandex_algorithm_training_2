# Python 3.12.1
# Сперва пошёл по пути целочисленного деления, но из-за целочисленного деления в (first_electoral = sum_of_votes / place) может возникнуть бесконечный цикл, тут нужно использовать обычное деление и тогда решение проходит
# мне понравилось моё решение на словарях, легче читать чем на списке

parts = dict()
sum_of_votes = 0
place = 450
first_electoral = 0
answer = dict()

with open('C:/python/yandex_algo_trainee_v2/input.txt', 'rt', encoding = 'utf-8') as file_input:
    for line in file_input:
        line = line.split()
        cnt = int(line[-1])
        name = ' '.join(line[:-1])
        parts[name] = parts.get(name, 0) + cnt
        sum_of_votes += cnt

first_electoral = sum_of_votes / place
print(first_electoral)
for party in parts:
    t = parts[party] // first_electoral
    print(t)
    answer[party] = answer.get(party, 0) + (t)
    place -= t

priority = sorted(answer, key = lambda p: (-(parts[p] % first_electoral), -parts[p]))
cnt_parties = len(priority)
counter = 0
while place:
    answer[priority[counter % cnt_parties]] += 1
    place -= 1
    counter += 1

result = []
for party in answer:
    result.append(f'{party} {int(answer[party])}')

print('\n'.join(result))
