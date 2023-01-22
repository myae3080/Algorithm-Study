# source : https://www.acmicpc.net/problem/9550

# input
k = int(input())
a, b = map(int, input().split())

if a == b:
    print(k ** 2)
else:
    print(k ** 2 - ((abs(a - b) / 2) ** 2))