# Python 3.12.1

arr_1 = list(map(int, input().split()))
ans = []
already_see = set()

for num in range(len(arr_1)):
    if arr_1[num] not in already_see and arr_1[num] not in set(arr_1[num+1:]):
        ans.append(arr_1[num])
    already_see.add(arr_1[num])

print(*ans)
