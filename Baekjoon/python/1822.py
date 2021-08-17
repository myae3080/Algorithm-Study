# source : https://www.acmicpc.net/problem/1822
# data structure, sorting

# list로 풀려했다가 시간초과.

# input
a, b = map(int, input().split())
a_set = set(map(int, input().split()))
b_set = set(map(int, input().split()))

result = list(a_set - b_set)

print(len(result))
[print(i, end=' ') for i in sorted(result)]