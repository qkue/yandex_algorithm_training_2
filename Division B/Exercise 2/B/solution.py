# Python 3.12.1
# В решениях от лектора приводится решение за два прохода, что будет быстрее этого квадратичного, но немного длиннее в реализации

arr = list(map(int, input().split()))
result = 0
for house in range(len(arr)):
    if arr[house] == 1:
        dist = 20
        for building in range(len(arr)):
            if arr[building] == 2 and abs(house - building) < dist:
                dist = abs(house - building)

        if result < dist:
            result = dist

print(result)
