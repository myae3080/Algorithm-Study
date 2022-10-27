# source : https://www.acmicpc.net/problem/14487

# input
n = int(input())
costs = list(map(int, input().split()))

result = 50000 * 1000
total = sum(costs)
for cost in costs:
    result = min(result, total - cost)

print(result)