# Python 3.12.1
# простое и элегантное решение

s = input()
k = 0
for b in s:
    k += [-1, 1][b == '(']
    if k < 0:
        break
print(['NO', 'YES'][k == 0])
