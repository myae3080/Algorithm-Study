# source : https://leetcode.com/problems/number-of-islands/

class Solution:
    # inefficient
    def numIslands(self, grid: list[list[str]]) -> int:
        x_limit, y_limit = len(grid), len(grid[0])
        visit, visited = set(), set()
        island = 0
        directions = [
            [1, 0],
            [-1, 0],
            [0, 1],
            [0, -1]
        ]
        
        for i in range(x_limit):
            for j in range(y_limit):
                val = grid[i][j]
                
                if val == "1" and (i, j) not in visited:
                    visit.add((i, j))
                    
                    while visit:
                        temp = visit.pop()
                        visited.add(temp)
                        
                        for d in directions:
                            new_x, new_y = temp[0] + d[0], temp[1] + d[1]
                            
                            if (x_limit > new_x >= 0 and y_limit > new_y >= 0) and (new_x, new_y) not in visited and grid[new_x][new_y] == "1":
                                visit.add((new_x, new_y))
                                
                    island += 1
                    
        return island