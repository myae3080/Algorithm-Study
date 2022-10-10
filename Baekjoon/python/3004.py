# source : https://www.acmicpc.net/problem/3004

# input
n = int(input())
cut = n // 2

if n % 2:
    print((cut + 1) * (cut + 2))
else:
    print((cut + 1) ** 2)