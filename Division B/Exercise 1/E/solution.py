# Python 3.12.1

d = int(input())
x, y = map(int, input().split())

if x >= 0 and y >= 0 and x + y <= d:
    print(0)
else:    
    a = ((x - 0) ** 2 + (y - 0) ** 2, 1)
    b = ((x - d) ** 2 + (y - 0) ** 2, 2)
    c = ((x - 0) ** 2 + (y - d) ** 2, 3)
    ans = min([a, b, c])
    print(ans[1])
