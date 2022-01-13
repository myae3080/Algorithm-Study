# source : https://leetcode.com/problems/first-unique-character-in-a-string/

class Solution:
    # inefficient
    def firstUniqChar(self, s: str) -> int:
        target = ''
        
        for c in s:
            if s.count(c) == 1:
                target = c
                break
        
        if target:
            return s.index(target)
        else:
            return -1