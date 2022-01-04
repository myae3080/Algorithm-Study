# source : https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> list[str]:
        result = []
        
        def dfs(idx = 0, string = ''):
            if idx < len(s):
                temp = s[idx]
                
                if temp.isdigit():
                    dfs(idx + 1, string + temp)
                else:
                    dfs(idx + 1, string + temp)
                    
                    if temp.islower():
                        dfs(idx + 1, string + temp.upper())
                    else:
                        dfs(idx + 1, string + temp.lower())
            else:
                result.append(string)
                
        dfs()
        
        return result