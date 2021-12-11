# source : https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        for i in range(1, len(nums)):
            temp_num = nums[i - 1]
            
            if temp_num > 0:
                nums[i] += temp_num
        
        return max(nums)