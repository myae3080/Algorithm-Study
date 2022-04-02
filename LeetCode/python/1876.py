# source : https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        result = 0
        
        for i in range(len(s) - 2):
            target = list(s[i:i + 3])
            
            if len(target)  == len(set(target)):
                result += 1
                
        return result
    
    def countGoodSubstrings2(self, s: str) -> int:
        result = 0
        
        for i in range(len(s) - 2):
            first, second, third = s[i], s[i + 1], s[i + 2]
            
            if first != second and first != third and second != third:
                result += 1
                
        return result