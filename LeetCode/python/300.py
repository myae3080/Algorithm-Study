# source : https://leetcode.com/problems/longest-increasing-subsequence/

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        length = len(nums)
        dp = [1] * length
        
        for i in range(length):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                
        return max(dp)