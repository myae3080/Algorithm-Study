# source : https://www.acmicpc.net/problem/25628

# input
bread, patty = map(int, input().split())

if bread // 2 == 0 or patty == 0:
    print(0)
else:
    print(min(bread // 2, patty))