# Python 3.9 (PyPy 7.3.11)

s = int(input())

a = [(value, num) for num, value in enumerate(map(int, input().split()[1:]))]
a.sort()
b = [(value, num) for num, value in enumerate(map(int, input().split()[1:]))]
b.sort()
c = [(value, num) for num, value in enumerate(map(int, input().split()[1:]))]
c.sort(key = lambda p: (p[0], -p[1]))
len_c = len(c) - 1
flag = False

for a_val, a_pos in a:
    c_pos = len_c
    for b_val, b_pos in b:
        while c_pos > 0 and a_val + b_val + c[c_pos][0] > s:
            c_pos -= 1
        if a_val + b_val + c[c_pos][0] == s and (not flag or (a_pos, b_pos, c_pos) < ans):
            ans = a_pos, b_pos, c[c_pos][1]
            flag = True
            

if flag:
    print(*ans)
else:
    print(-1)
