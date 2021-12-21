# source : https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        start_visit, visit, visited = [], [], set()
        x_limit, y_limit = len(grid), len(grid[0])
        directions = [
            [-1, 0],
            [1, 0],
            [0, -1],
            [0, 1],
        ]
        count = 0
        
        for i in range(x_limit):
            for j in range(y_limit):
                if grid[i][j] == 2:
                    start_visit.append([i, j])
                    
        if len(start_visit) != 0:
            visit.append(start_visit)
        
        while visit:
            temp_visit = []
            temp = visit.pop()
            is_rotten = False

            for li in temp:
                visited.add((li[0], li[1]))

                for d in directions:
                    new_x, new_y = li[0] + d[0], li[1] + d[1]

                    if (x_limit > new_x >= 0 and y_limit > new_y >= 0) and grid[new_x][new_y] == 1 and (new_x, new_y) not in visited:
                        is_rotten = True
                        grid[new_x][new_y] = 2
                        temp_visit.append([new_x, new_y])

            if len(temp_visit) != 0:
                visit.append(temp_visit)

            if is_rotten:
                count += 1
                    
                           
        
        # 정상 오렌지 체크
        for i in range(x_limit):
            if grid[i].count(1):
                return -1
            
        return count