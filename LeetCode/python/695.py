# source : https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        visit, visited = set(), set()
        max_island = 0
        x_limit, y_limit = len(grid), len(grid[0])
        directions = [
            [-1, 0],
            [0, -1],
            [1, 0],
            [0, 1]
        ]
        
        for x in range(x_limit):
            for y in range(y_limit):
                if (x, y) not in visited and grid[x][y] == 1:
                    island = 0
                    visit.add((x, y))
                    
                    while visit:
                        temp = visit.pop()
                        visited.add(temp)
                        island += grid[temp[0]][temp[1]]
            
                        for a, b in directions:
                            temp_x, temp_y = temp[0] + a, temp[1] + b
                        
                            if (x_limit > temp_x >= 0 and y_limit > temp_y >= 0) and (temp_x, temp_y) not in visited and grid[temp_x][temp_y] == 1:
                                visit.add((temp_x, temp_y))

                    max_island = max(max_island, island)
                            
        return max_island