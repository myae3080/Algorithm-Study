# source : https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        num_count = len(nums)
        
        if num_count == 1:
            return True
        
        is_reachable = False
        dp = [0] * (num_count - 1)
        dp[0] = nums[0]
        
        for i in range(1, num_count - 1):
            dp[i] = max(nums[i], dp[i - 1] - 1)
            
        if 0 not in dp:
            is_reachable = True
            
        return is_reachable