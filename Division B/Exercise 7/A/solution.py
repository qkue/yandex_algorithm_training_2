# Python 3.12.1

d = int(input())
answer = 0
arr = sorted(tuple(map(int, input().split())) for _ in range(d))

left = - 10 ** 10

for i in range(d):
    
    x, y = arr[i]
    if left < x:
        left = x
    elif left > y:
        y = left
    answer += (y - left)
    left = y

print(answer)
