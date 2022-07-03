# source : https://www.acmicpc.net/problem/1834
# math

# input
n = int(input())

print(sum([i for i in range(n + 1, n ** 2, n + 1) if (i // n) == (i % n)]))