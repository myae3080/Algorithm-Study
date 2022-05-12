# source : https://leetcode.com/problems/self-dividing-numbers/

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        result = []
        
        for n in range(left, right + 1):
            is_valid = True
            
            if n % 10 != 0:
                for i in set(list(str(n))):
                    if i == '0' or n % int(i) != 0:
                        is_valid = False
                        break

                if is_valid:
                    result.append(n)
                
        return result