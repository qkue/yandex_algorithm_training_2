# Python 3.12.1

a, b, c, d = map(int, input().split())

def check(x):
    if a > 0:
        return (a*x*x*x + b*x*x + c*x + d) <= 0
    else:
        return (a*x*x*x + b*x*x + c*x + d) >= 0
        
right = 2000
left = -2000

while (left + 0.000000001) < right:
    m = (left + right) / 2
    if check(m):
        left = m
    else:
        right = m
print(left) 
