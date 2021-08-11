# source : https://www.acmicpc.net/problem/2217
# math, greedy, sorting, physics

# input
rope = sorted([int(input()) for _ in range(int(input()))], reverse=True)

for i in range(len(rope)):
    rope[i] = (i + 1) * rope[i]

print(max(rope))