# source : https://leetcode.com/problems/check-if-it-is-a-straight-line/

class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        base_x, base_y = coordinates[0][0], coordinates[0][1]
        dx, dy = base_x - coordinates[1][0], base_y - coordinates[1][1]
        
        for coordinate in coordinates[2:]:
            temp_x, temp_y = coordinate[0], coordinate[1]
            
            if dx * (base_y - temp_y) != dy * (base_x - temp_x):
                return False
            
        return True