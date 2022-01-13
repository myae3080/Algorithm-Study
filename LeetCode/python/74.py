# source : https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        for li in matrix:
            if target in li:
                return True
                
        return False