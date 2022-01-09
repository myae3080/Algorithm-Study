# source : https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        for i in range(1, len(nums)):
            temp_num = nums[i - 1]
            
            if temp_num > 0:
                nums[i] += temp_num
        
        return max(nums)

    def maxSubArray2(self, nums: list[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            
        return max(dp)