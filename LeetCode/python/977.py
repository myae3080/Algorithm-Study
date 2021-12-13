# source : https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        squared_list = [n ** 2 for n in nums]
        
        return sorted(squared_list)