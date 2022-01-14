# source : https://leetcode.com/problems/ransom-note/

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:        
        count = 0
        
        for c in ransomNote:
            if magazine.find(c) != -1:
                magazine = magazine.replace(c, '', 1)
                count += 1
        
        if len(ransomNote) == count:
            return True
        else:
            return False