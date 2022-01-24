# source : https://leetcode.com/problems/climbing-stairs/

class Solution:
    # 1st
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1
        
        if n >= 2:
            dp[2] = 2
            
            for i in range(3, n + 1):
                dp[i] = dp[i - 2] + dp[i - 1]
        
        return dp[n]
    
    # 2nd
    def climbStairs(self, n: int) -> int:
        dp = [1] * (n + 1)
            
        for i in range(2, n + 1):
            dp[i] = dp[i - 2] + dp[i - 1]
        
        return dp[n]