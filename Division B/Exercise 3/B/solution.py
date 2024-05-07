# Python 3.12.1

arr_1 = list(map(int, input().split()))
ans = []
we_meet = set()

for num in arr_1:
    if num in we_meet:
        ans.append('YES')
    else:
        ans.append('NO')
    we_meet.add(num)
    
print('\n'.join(ans))
