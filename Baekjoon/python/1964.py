# source : https://www.acmicpc.net/problem/1964

# input
n = int(input())

print((1 + ((2 * 4 + (n - 1) * 3) * n // 2)) % 45678)