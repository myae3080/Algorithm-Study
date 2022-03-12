# source : https://leetcode.com/problems/monotonic-array/

class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        if nums != sorted(nums) and nums != sorted(nums, reverse=True):
            return False
        
        return True