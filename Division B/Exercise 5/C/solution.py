# Python 3.12.1

n, m = map(int, input().split())
x = sorted([key, value] for value, key in enumerate(map(int, input().split()), 1))
y = sorted([key - 1, value] for value, key in enumerate(map(int, input().split()), 1))


group_cnt = 0
comp_cnt = 0

while group_cnt < n and comp_cnt < m:
    
    if x[group_cnt][0] <= y[comp_cnt][0]:
        x[group_cnt].append(y[comp_cnt][1])
        group_cnt += 1
    
    comp_cnt += 1

while group_cnt < n:
    x[group_cnt].append(0)
    group_cnt += 1

x.sort(key = lambda p: p[1])
answer = []
len_answer = 0
for stud in x: 
    count = stud[2]
    answer.append(count)
    len_answer += 1 if count > 0 else 0
print(len_answer)
print(*answer)
