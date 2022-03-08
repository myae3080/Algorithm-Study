# source : https://leetcode.com/problems/verifying-an-alien-dictionary/

class Solution:
    def isAlienSorted(self, words: list[str], order: str) -> bool:
        is_valid = True
        
        for i in range(len(words) - 1):
            a, b = words[i], words[i + 1]
            
            for j in range(min(len(a), len(b))):
                if a[j] != b[j]:
                    if order.index(a[j]) > order.index(b[j]):
                        is_valid = False
                    
                    break
            
            if is_valid and b in a and a != b:
                is_valid = False
                    
        return is_valid