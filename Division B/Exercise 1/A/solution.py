# Python 3.12.1

r = int(input()) # task
i = int(input()) # interactor
c = int(input()) # checker
ans = None

if i == 0 or i == 4:
    if r != 0:
        ans = 3
    else:
        ans = c if i == 0 else 4
elif i == 1:
    ans = c
elif i == 6:
    ans = 0
elif i == 7:
    ans = 1
else:
    ans = i

print(ans)
