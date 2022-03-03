# source : https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        c1, c2 = list(s1), list(s2)
        count = 0
        
        if sorted(c1) != sorted(c2):
            return False
        
        for i in range(len(c1)):
            if c1[i] != c2[i]:
                count += 1
                
        return False if count > 2 else True