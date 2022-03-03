# source : https://leetcode.com/problems/happy-number/

class Solution:
    def isHappy(self, n: int) -> bool:
        dup_check = set()
        
        while n != 1 and n not in dup_check:
            dup_check.add(n)
            temp = 0
            
            for num in list(str(n)):
                temp += int(num) ** 2
            
            n = temp
            
        return True if n == 1 else False