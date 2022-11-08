# source : https://www.acmicpc.net/problem/2399

# PyPy3로 통과
# input
n = int(input())
coordinates = list(map(int, input().split()))

result = 0
for i in coordinates:
    for j in coordinates:
        result += abs(i - j)

print(result)