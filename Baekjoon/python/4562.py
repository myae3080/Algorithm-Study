# source : https://www.acmicpc.net/problem/4562

for _ in range(int(input())):
    # input
    x, y = map(int, input().split())

    print('MMM BRAINS') if x >= y else print('NO BRAINS')