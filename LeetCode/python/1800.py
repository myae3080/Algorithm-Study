# source : https://leetcode.com/problems/maximum-ascending-subarray-sum/\
    
class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        length = len(nums)
        dp = [0] * length
        dp[0] = nums[0]
        
        for i in range(1, length):
            if nums[i] > nums[i - 1]:
                dp[i] = dp[i - 1] + nums[i]
            else:
                dp[i] = nums[i]

        return max(dp)