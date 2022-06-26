# source : https://www.acmicpc.net/problem/17173

# input
n, m = map(int, input().split())
nums = list(map(int, input().split()))

results = set()

for i in range(1, n + 1):
    for num in nums:
        if i % num == 0:
            results.add(i)

print(sum(results))