# source : https://www.acmicpc.net/problem/4963
# bfs, dfs

directions = [
    (-1, -1), (1, -1), (-1, 1), (1, 1),
    (0, -1), (-1, 0), (0, 1), (1, 0)
]

while True:
    # input
    w, h = map(int, input().split())
    
    if w == 0 and h == 0:
        break
    
    # input
    locations = [list(map(int, input().split())) for _ in range(h)]
    
    islands = 0
    visited = []
    
    for i in range(h):
        for j in range(w):
            location = locations[i][j]
            
            if location == 1 and (i, j) not in visited:
                islands += 1
                to_visit = [(i, j)]
                
                while to_visit:
                    curr = to_visit.pop()
                    visited.append(curr)
                    
                    for dir in directions:
                        new_x, new_y = curr[0] + dir[0], curr[1] + dir[1]
                        
                        if (0 <= new_x < h and 0 <= new_y < w) and locations[new_x][new_y] == 1 and (new_x, new_y) not in visited:
                            to_visit.append((new_x, new_y))
    
    print(islands)