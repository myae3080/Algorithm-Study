# source : https://www.acmicpc.net/problem/2740

# input
n, m = map(int, input().split())
matrix1 = [list(map(int, input().split())) for _ in range(n)]
m, k = map(int, input().split())
matrix2 = [list(map(int, input().split())) for _ in range(m)]

result_matrix = [[0] * k for _ in range(n)]

for i in range(n):
    for j in range(k):
        for l in range(m):
            result_matrix[i][j] += matrix1[i][l] * matrix2[l][j]

for row in result_matrix:
    for num in row:
        print(num, end=' ')
    print()