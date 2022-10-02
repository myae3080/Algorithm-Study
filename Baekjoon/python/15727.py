# source : https://www.acmicpc.net/problem/15727

# input
n = int(input())

print((n // 5) + (1 if n % 5 else 0))