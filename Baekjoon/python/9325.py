# source : https://www.acmicpc.net/problem/9325
# math

for _ in range(int(input())):
    # input
    total = int(input())

    for __ in range(int(input())):
        # input
        count, option_price = map(int, input().split())

        total += count * option_price

    print(total)