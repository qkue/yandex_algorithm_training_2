# Python 3.12.1

n = int(input())
arr = list(map(int, input().split()))
m = int(input())
seq_m = list(map(int, input().split()))

for target in seq_m:
    left = 0
    right = n - 1
    while left < right:
        m = (left + right) // 2
        if arr[m] >= target:
            right = m
        else:
            left = m + 1
    left_ans = left + 1
    if arr[left] != target:
        left_ans = 0

    left_second = 0
    right_second = n - 1
    while left_second < right_second:
        m_second = (left_second + right_second + 1) // 2
        if arr[m_second] <= target:
            left_second = m_second
        else:
            right_second = m_second - 1
    right_ans = left_second + 1
    if arr[left_second] != target:
        right_ans = 0

    print(left_ans, right_ans)
