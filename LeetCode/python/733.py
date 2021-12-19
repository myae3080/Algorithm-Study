# source : https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, newColor: int) -> list[list[int]]:
        x_limit, y_limit = len(image), len(image[0])
        start_color, image[sr][sc] = image[sr][sc], newColor
        visited, visit = [], []
        visit.append([sr, sc])
        visited.append([sr, sc])
        directions = [
            [-1, 0],
            [0, -1],
            [1, 0],
            [0, 1]
        ]
        
        while visit:
            temp = visit.pop()
            
            for dir in directions:
                x, y = temp[0] + dir[0], temp[1] + dir[1]
                
                if (x_limit > x >= 0 and y_limit > y >= 0) and [x, y] not in visited:
                    if image[x][y] == start_color:
                        print(x, y)
                        image[x][y] = newColor
                        visit.append([x, y])
                        visited.append([x, y])
                        
        return image