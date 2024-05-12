# Python 3.12.1


n = int(input())
piece = []
answer = []

# берем данные из ввода
value_input = input()
while  value_input != '0 0':
    L, R = map(int, value_input.split())
    if L < n and R > 0:
        piece.append((L, R))
    value_input = input()
piece.sort()

# основной цикл, в котором покрываем прямую с первого элемента
current_right = 0
current_max = (0, 0)
for line in piece:
    L, R = line
    if L > current_right:
        answer.append(current_max)
        current_right = current_max[1]
        if current_right >= n:
            break

    if L <= current_right and R > current_max[1]:
        current_max = line

if current_right < n:
    answer.append(current_max)
    current_right = current_max[1]

if current_right >= n:
    answer.sort()
    print(len(answer))
    print('\n'.join(str(left) + ' ' + str(right) for left, right in answer))
else:
    print('No solution')
