# source : https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        # exception handling
        if not digits:
            return []
        
        dic = {
            "2": "abc", "3": "def", "4": "ghi",
            "5": "jkl", "6": "mno", "7": "pqrs",
            "8": "tuv", "9": "wxyz"
        }
        
        length = len(digits)
        result = []
        
        def dfs(word, idx = 0):
            if len(word) == length:
                result.append(word)
                return
            
            for i in range(idx, length):
                for c in dic[digits[i]]:
                    dfs(word + c, i + 1)
                    
        dfs("")
                    
        return result