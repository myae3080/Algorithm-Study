# source : https://www.acmicpc.net/problem/13410

# input
n, k = map(int, input().split())

print(max([int(str(n * i)[::-1]) for i in range(1, k + 1)]))