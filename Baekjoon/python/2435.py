# source : https://www.acmicpc.net/problem/2435

# input
n, k = map(int, input().split())
temparatures = list(map(int, input().split()))

result = -(10 ** 5)
for i in range(n - k + 1):
    result = max(result, sum(temparatures[i:i + k]))

print(result)