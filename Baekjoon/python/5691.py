# source : https://www.acmicpc.net/problem/5691

while 1:
    # input
    a, b = map(int, input().split())

    if a == b == 0:
        break

    print(a - (b - a))