# source : https://www.acmicpc.net/problem/5054

for _ in range(int(input())):
    # input
    n = int(input())
    stores = sorted(list(map(int, input().split())))
    print((stores[-1] - stores[0]) * 2)