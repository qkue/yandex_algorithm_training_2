# Python 3.12.1

n= int(input())
arr = list(map(int, input().split()))
current_sum = 0
max_sum = arr[0]

for element in arr:
    current_sum += element
    max_sum = max(max_sum, current_sum)
    current_sum = max(current_sum, 0)

print(max_sum)
