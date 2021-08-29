# source : https://www.acmicpc.net/problem/2476
# math

amount = []

for _ in range(int(input())):
    # input
    a, b, c = map(int, input().split())

    if a == b == c:
        amount.append(10000 + a * 1000)
        continue
    elif a == b or a == c:
        amount.append(1000 + a * 100)
        continue
    elif b == c:
        amount.append(1000 + b * 100)
        continue
    else:
        amount.append(max(a, b, c) * 100)
        continue

print(max(amount))