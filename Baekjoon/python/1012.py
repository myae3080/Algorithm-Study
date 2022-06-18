# source : https://www.acmicpc.net/problem/1012

directions = [
    [-1, 0],
    [0, -1],
    [1, 0],
    [0, 1]
]

for _ in range(int(input())):
    # input
    m, n, k = map(int, input().split())
    
    field = [[0] * n for _ in range(m)]
    earthworms = 0
    checked, to_check = [], []
    
    for __ in range(k):
        # input
        x, y = map(int, input().split())
        
        field[x][y] = 1
        
    '''
        time complexity : O(n^2)
        space complexity : O(n)
    '''
    for i in range(m):
        for j in range(n):
            if field[i][j] == 1 and (i, j) not in checked:
                to_check.append((i, j))
                earthworms += 1
                
                while to_check:
                    location = to_check.pop()
                    checked.append(location)
                    
                    for d in directions:
                        row, col = location[0] + d[0], location[1] + d[1]
                        
                        if (0 <= row < m and 0 <= col < n) and field[row][col] == 1 and (row, col) not in checked:
                            to_check.append((row, col))
    
    print(earthworms)