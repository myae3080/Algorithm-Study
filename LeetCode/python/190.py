# source : https://leetcode.com/problems/reverse-bits/

class Solution:
    def reverseBits(self, n: int) -> int:
        binary = bin(n)[2:][::-1]
        
        result = binary + "0" * (32 - len(binary))
        
        return int(result, 2)