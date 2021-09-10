# source : https://www.acmicpc.net/problem/10984
# math

for _ in range(int(input())):
    n, total = 0, 0

    for _ in range(int(input())):
        # input
        c, g = map(float, input().split())

        n += c
        total += c * g

    print(int(n), round(total / n, 1))