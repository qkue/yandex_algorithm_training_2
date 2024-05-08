# Python 3.12.1
# видимо подняли лимит по времени, моё решение некоторые тесты проходило по 1.3+ сек

n, q = map(int, input().split())
arr = list(map(int, input().split()))

prefixsum = [0] * (n + 1)
for i in range(1, n + 1):
    prefixsum[i] = prefixsum[i - 1] + arr[i - 1]

for _ in range(q):
    left, right = map(int, input().split())
    print(prefixsum[right] - prefixsum[left - 1])
