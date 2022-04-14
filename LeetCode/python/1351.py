# source : https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/

class Solution:
    def countNegatives(self, grid: list[list[int]]) -> int:
        result = 0
        
        for li in grid:
            size = len(li)
            
            for i, n in enumerate(li):
                if n < 0:
                    result += size - i
                    break
                    
        return result