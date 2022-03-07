# source : https://leetcode.com/problems/find-the-difference/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_list, t_list = sorted(list(s)), sorted(list(t))
        
        for i in range(len(s)):
            if s_list[i] != t_list[i]:
                return t_list[i]
            
        return t_list[-1]