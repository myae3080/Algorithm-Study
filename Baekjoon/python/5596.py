# source : https://www.acmicpc.net/problem/5596
# math

# input
s = sum(list(map(int, input().split())))
t = sum(list(map(int, input().split())))

print(s) if s >= t else print(t)