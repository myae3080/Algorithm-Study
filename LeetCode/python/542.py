# source : https://leetcode.com/problems/01-matrix/

class Solution:
    # 기존 방식은 사방위로 체크하며 진행했지만, 아직 체크 되지 않은 좌표를 체크하면서 몇몇 부분이 계속 틀려서 양방향으로부터 체크하는 방식으로 풀이.
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        x_limit, y_limit = len(mat), len(mat[0])
        
        dp = [[10001] * y_limit for _ in range(x_limit)]
        
        for i in range(x_limit):
            for j in range(y_limit):
                if mat[i][j] != 0:
                    if i - 1 >= 0:
                        dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)
                        
                    if j - 1 >= 0:
                        dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)
                else:
                    dp[i][j] = 0
                    
        for i in range(x_limit - 1, -1, -1):
            for j in range(y_limit - 1, -1, -1):
                if mat[i][j] != 0:
                    if x_limit > i + 1:
                        dp[i][j] = min(dp[i][j], dp[i + 1][j] + 1)
                        
                    if y_limit > j + 1:
                        dp[i][j] = min(dp[i][j], dp[i][j + 1] + 1)
                else:
                    dp[i][j] = 0
                    
        return dp