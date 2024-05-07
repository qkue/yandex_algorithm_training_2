# Python 3.12.1

n = int(input())
arr = list(map(int, input().split()))
ans = 0
max_folder = 0

for folder in arr:
    if folder > max_folder:
        max_folder = folder
        
    ans += folder
ans -= max_folder
print(ans)
