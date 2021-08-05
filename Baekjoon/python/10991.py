# source : https://www.acmicpc.net/problem/10991
# star

# input
n = int(input())

[print(' ' * (n - i) + '* ' * i) for i in range(1, n + 1)]
