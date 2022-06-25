# source : https://www.acmicpc.net/problem/13866

# input
level = list(map(int, input().split()))

print(abs((level[-1] + level[0]) - sum(level[1:-1])))