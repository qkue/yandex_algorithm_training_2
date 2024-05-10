# Python 3.12.1

d = int(input())
x, y = map(int, input().split())

if x >= 0 and y >= 0 and x + y <= d:
    print(0)
else:
    a = (1, (x - 0) ** 2 + (y - 0) ** 2)
    b = (2, (x - d) ** 2 + (y - 0) ** 2)
    c = (3, (x - 0) ** 2 + (y - d) ** 2)
    ans = min([a, b, c], key = lambda p: (p[1], p[0]))
    print(ans[0])
