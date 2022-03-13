# https://leetcode.com/problems/repeated-substring-pattern/

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(1, (len(s) // 2) + 1):
            temp = s[:i]
            
            if  s.find(temp) != -1 and temp * (len(s) // len(temp)) == s:
                return True
        
        return False