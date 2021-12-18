# source : https://leetcode.com/problems/permutation-in-string/

from itertools import permutations

class Solution:
    # time limit exceeded
    def checkInclusion(self, s1: str, s2: str) -> bool:
        for li in permutations(list(s1), len(s1)):
            if ''.join(li) in s2:
                return True
            
    # inefficient solution
    def checkInclusion2(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s1_list = sorted(list(s1))
        is_true = False
        
        if len(s2) != 1:
            for i in range(len(s2) - 1):
                temp = list(s2[i:i + s1_len])

                if sorted(temp) == s1_list:
                    is_true = True
                    break
        else:
            if s1 == s2:
                is_true = True
            else:
                is_true = False
        
        return is_true