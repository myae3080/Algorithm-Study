# source : https://www.acmicpc.net/problem/15819
# string, sorting

# input
n, i = map(int, input().split())

print(sorted([input() for _ in range(n)])[i - 1])