# source : https://www.acmicpc.net/problem/17247
# math

# input
y, x = map(int, input().split())

coordinate, pointers = [], []

[coordinate.append(list(map(int, input().split()))) for _ in range(y)]

for i in range(y):
    for j in range(x):
        if coordinate[i][j]:
            pointers.append([i, j])

print(abs(pointers[0][0] - pointers[1][0]) + abs(pointers[0][1] - pointers[1][1]))