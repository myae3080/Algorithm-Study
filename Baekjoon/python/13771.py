# source : https://www.acmicpc.net/problem/13771
# sorting

prices = []

# input
[prices.append(float(input())) for _ in range(int(input()))]

prices.sort()

print(format(prices[1], ".2f"))