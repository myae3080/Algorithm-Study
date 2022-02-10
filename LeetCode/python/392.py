# source : https://leetcode.com/problems/is-subsequence/submissions/

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        chars = list(s)
        
        for c in t:
            if chars and c == chars[0]:
                chars.pop(0)
        
        if not chars:
            return True 
        else:
            return False