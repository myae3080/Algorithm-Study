# source :https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: list[int]) -> int:
        length = len(height)
        dp = [0] * length
        left, right = 0, 0
        
        for i in range(length):
            if height[i] < left:
                dp[i] = left - height[i]
            else:
                left = height[i]
                
        for i in range(length - 1, -1, -1):
            if height[i] < right:
                dp[i] = min(dp[i], right - height[i])
            else:
                right = height[i]
                dp[i] = 0

        return sum(dp)