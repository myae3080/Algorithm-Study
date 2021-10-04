# source : https://www.acmicpc.net/problem/17263

# input
n = int(input())
num_list = list(map(int, input().split()))

print(sorted(num_list)[n - 1])