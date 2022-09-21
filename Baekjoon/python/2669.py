# source : https://www.acmicpc.net/problem/2669

coordinates = [[0] * 101 for _ in range(101)]
result = 0

for _ in range(4):
    # input
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(x1, x2):
        for j in range(y1, y2):
            if coordinates[i][j] == 0:
                result += 1
                coordinates[i][j] = 1

print(result)