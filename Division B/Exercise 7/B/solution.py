# Python 3.12.1

n = int(input())
times = []
answer = 0
max_result = 0

for _ in range(n):
    t, L = map(int, input().split())
    times.append((t, 1)) # IN
    times.append((t + L, -1)) # OUT

times.sort()

for goods in times:
    if goods[1] == 1:
        answer += 1
        max_result = max(max_result, answer)
    elif goods[1] == -1:
        answer -= 1
    
    max_result = max(max_result, answer)

print(max_result)    
