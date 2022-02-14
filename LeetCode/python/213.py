# source : https://leetcode.com/problems/house-robber-ii/

class Solution:
    # inefficient
    def rob(self, nums: list[int]) -> int:
        size = len(nums)
        first_dp, second_dp = [0] * size, [0] * size
        
        first_dp[0] = nums[0]
        
        if size > 1:
            first_dp[1] = nums[0]
            second_dp[1] = nums[1]
        
        for i in range(2, size):
            if i != size - 1:
                first_dp[i] = max(first_dp[i - 2] + nums[i], first_dp[i - 1])
                
            second_dp[i] = max(second_dp[i - 2] + nums[i], second_dp[i - 1])
            
        return max(max(first_dp), max(second_dp))