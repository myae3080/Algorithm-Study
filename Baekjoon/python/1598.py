# source : https://www.acmicpc.net/problem/1598

# input
a, b = map(int, input().split())

a -= 1
b -= 1

row_distance = abs(b // 4 - a // 4)
col_distance = abs(b % 4 - a % 4)

print(row_distance + col_distance)