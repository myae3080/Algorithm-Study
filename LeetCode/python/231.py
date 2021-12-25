# source : https://leetcode.com/problems/power-of-two/

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        print(str(bin(n)))
        if n < 0:
            return False
        else:
            if str(bin(n)).count('1') == 1:
                return True
            else:
                return False