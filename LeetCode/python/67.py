# source : https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def toDecimal(num: str) -> int:
            decimal = 0
            digits = len(num)

            for i in range(digits):
                decimal += int(num[i]) * (2 ** (digits - 1 - i))

            return decimal
        
        return bin(toDecimal(a) + toDecimal(b))[2:]