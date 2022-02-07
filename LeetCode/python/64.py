# source : https://leetcode.com/problems/minimum-path-sum/

class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        x_range, y_range = len(grid[0]), len(grid)
        dp = [[0 for _ in range(x_range)] for _ in range(y_range)]
        
        for i in range(y_range):
            for j in range(x_range):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                else:
                    if i != 0 and j != 0:
                        dp[i][j] = min(dp[i - 1][j] + grid[i][j], dp[i][j - 1] + grid[i][j])
                    else:
                        if i != 0:
                            dp[i][j] = dp[i - 1][j] + grid[i][j]
                        else:
                            dp[i][j] = dp[i][j - 1] + grid[i][j]
        
        return dp[-1][-1]