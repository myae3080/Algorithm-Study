# source : https://www.acmicpc.net/problem/2160

drawings = []

# input
n = int(input())
[drawings.append([list(input()) for __ in range(5)]) for _ in range(n)]
    
drawing1 = drawing2 = 0
min = 36

for i in range(n):
    for j in range(i + 1, n):
        count = 0
        
        for r in range(5):
            for c in range(7):
                if drawings[i][r][c] != drawings[j][r][c]:
                    count += 1
    
        if count < min:
            min = count
            drawing1, drawing2 = i + 1, j + 1

print(drawing1, drawing2)