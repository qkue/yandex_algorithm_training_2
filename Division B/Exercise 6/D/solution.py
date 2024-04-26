# Python 3.12.1

a, k, b, m, x = map(int, input().split())

left = 0
right = x

while left < right:
    mid = (left + right) // 2
    if (a * (mid - mid // k) + (b * (mid - mid // m))) >= x:
        right = mid
    else:
        left = mid + 1

print(left)
