# Python 3.12.1
# оказалась задача на динамическое программирование :-)

import sys
sys.setrecursionlimit(3000)

def walk(now, neighbors, size, visited):
    visited[now] = True
    best = 1
    max_1 = -1
    max_2 = -1
    size[now] = 1
    for next in neighbors[now]:
        if not visited[next]:
            best = max(walk(next, neighbors, size, visited), best)
            if size[next] > max_1:
                max_2 = max_1
                max_1 = size[next]
            elif size[next] > max_2:
                max_2 = size[next]
    best = max(best, max_1 + 1)
    best = max(best, max_1 + max_2 + 1)
    size[now] = max(size[now], max_1 + 1)
    
    return best

n = int(input())
neighbors = []

for _ in range(n + 1):
    neighbors.append([])

for _ in range(n - 1):
    a, b = map(int, input().split())
    neighbors[a].append(b)
    neighbors[b].append(a)

size = [0] * (n + 1)
visited = [False] * (n + 1)

print(walk(1, neighbors, size, visited))
