# source : https://www.acmicpc.net/problem/17829
# devide and conquer

matrix = []

def polling(matrix, n):
    if n == 1:
        return matrix[0][0]
    else:
        half = n // 2
        new_matrix = [[0] * half for _ in range(half)]
        
        for i in range(0, n, 2):
            for j in range(0, n, 2):
                new_matrix[i // 2][j // 2] = sorted([matrix[i][j], matrix[i + 1][j], matrix[i][j + 1], matrix[i + 1][j + 1]])[2]
    
        return polling(new_matrix, half)

# input
n = int(input())
[matrix.append(list(map(int, input().split()))) for _ in range(n)]

print(polling(matrix, n))