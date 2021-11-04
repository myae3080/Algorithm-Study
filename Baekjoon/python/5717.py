# source : https://www.acmicpc.net/problem/5717

while True:
    # input
    total = sum(list(map(int, input().split())))

    if total == 0:
        break
    else:
        print(total)