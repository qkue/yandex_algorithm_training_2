# Python 3.12.1

boxes = dict()
n = int(input())

for _ in range(n):
    key, value = map(int, input().split())
    if key not in boxes:
        boxes[key] = 0
    boxes[key] += value

answer = []
for key in sorted(boxes):
    answer.append(f'{key} {boxes[key]}')

print('\n'.join(answer))
