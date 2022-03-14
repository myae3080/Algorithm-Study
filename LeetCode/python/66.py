# source : https://leetcode.com/problems/plus-one/

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        return list(map(int, str(int(''.join([str(d) for d in digits])) + 1)))