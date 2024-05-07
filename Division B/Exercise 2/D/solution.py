# Python 3.12.1
# Можно было сделать за один цикл, когда мы ищем сначала правый минимум и легко можем вывести и левый максимум или проверить правый максимум на то что он середина, но мне захотелось за два прохода 

lenghth, k = map(int, input().split())
legs = list(map(int, input().split()))
answer = []

if lenghth % 2 == 1 and ((lenghth // 2) in legs):
    answer.append(lenghth // 2)

else:
    for left in range(lenghth // 2 - 1, -1, -1):
        if left in legs:
            answer.append(left)
            break
    for right in range(lenghth // 2, lenghth):
        if right in legs:
            answer.append(right)
            break

print(*answer)
