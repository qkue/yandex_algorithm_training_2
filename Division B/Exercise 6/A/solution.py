# Python 3.12.1

n = int(input())
arr = sorted(map(int, input().split()))
k = int(input())
ans = []

for elem in range(k):
        f_num, s_num = map(int, input().split())

        
        left = 0 
        right = n - 1
        while left < right:
            m = (left + right) // 2
            if arr[m] >= f_num:
                right = m
            else:
                left = m + 1
        # if arr[left] < f_num:
        #     left = n - 1

        left_second = 0
        right_second = n - 1
        while left_second < right_second:
            m = (left_second + right_second + 1) // 2
            #print(m)
            if arr[m] <= s_num:
                left_second = m
            else:
                right_second = m - 1
        # if arr[left]                 

        #print(f' L & R = {target[elem]}\n left = {left} left_second = {left_second}')
        #ans.append(left_second - left)
        if left_second != left or (left_second == left and arr[left_second] <= s_num and arr[left] >= f_num):
            ans.append(left_second - left + 1)
        else:
            ans.append(0)

print(*ans)
