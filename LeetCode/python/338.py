# source : https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> list[int]:
        return [bin(i)[2:].count("1") for i in range(0, n + 1)]