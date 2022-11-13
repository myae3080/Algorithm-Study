# source : https://www.acmicpc.net/problem/6131

# input
n = int(input())

result = 0
for B in range(1, 501):
    for A in range(1, 501):
        if (A ** 2) - (B ** 2) == n:
            result += 1

print(result)