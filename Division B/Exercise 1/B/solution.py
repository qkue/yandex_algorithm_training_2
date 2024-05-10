# Python 3.12.1

n, i, j = map(int, input().split())

if i > j:
    i, j = j, i

answer = min(j - i - 1, (i - 1) + (n - j))

print(answer)
