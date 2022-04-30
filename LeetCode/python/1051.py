# source : https://leetcode.com/problems/height-checker/

class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        result = 0
        sorted_heights = sorted(heights)
        
        for i in range(len(heights)):
            if heights[i] != sorted_heights[i]:
                result += 1
                
        return result