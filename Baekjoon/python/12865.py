# dp, 0 1 knapsack

import sys

# input
input = sys.stdin.readline

n, total_weight = map(int, input().split())
product_list = [[0, 0]]
[product_list.append(list(map(int, input().split()))) for i in range(n)]
product_list.sort()
knapsack = [[0] * (total_weight + 1) for i in range(n + 1)]

# 기본 공식으로 푸는 방식
for i in range(1, n + 1):
    for j in range(1, total_weight + 1):
        weight, value = product_list[i][0], product_list[i][1]

        if j >= weight:
            knapsack[i][j] = max(value + knapsack[i - 1][j - weight], knapsack[i - 1][j])
        else:
            knapsack[i][j] = knapsack[i - 1][j]

print(knapsack[n][total_weight])