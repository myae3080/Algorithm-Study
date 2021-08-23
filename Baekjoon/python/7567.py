# source : https://www.acmicpc.net/problem/7567
# string

height = 10

# input
bowl = list(input())

for i in range(1, len(bowl)):
    if bowl[i - 1] == bowl[i]:
        height += 5
    else:
        height += 10

print(height)