# source : https://www.acmicpc.net/problem/15633

# input
n = int(input())

result = []

for i in range(1, n + 1):
    if n % i == 0:
        result.append(i)

print(sum(result) * 5 - 24)