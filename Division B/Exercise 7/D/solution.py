# Python 3.12.1
# Задача немного коварная, точнее эта фраза "На прямой в точках a1, a2, …, an (возможно, совпадающих) сидят n котят." Имеется ввиду по одному котику сидит в точке

n, m = map(int, input().split())
events = []

for kitten in list(map(int, input().split())):
    events.append((kitten, 0))

for i in range(m):
    L, R = map(int, input().split())
    events.append((L, -1, i))
    events.append((R, 1, i))
events.sort()

kitty = 0
answer = [0] * m

for event in events:
    if event[1] == -1:
        answer[event[2]] -= kitty
    elif event[1] == 0:
        kitty += 1
    elif event[1] == 1:
        answer[event[2]] += kitty

print(*answer)
