# source : https://leetcode.com/problems/word-break/

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        length = len(s) + 1
        dp = [0] * length
        # dp 값이 1 다음 부터 단어의 시작
        dp[0] = 1
        
        for i in range(1, length):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = 1
                    break
                    
        return dp[-1]