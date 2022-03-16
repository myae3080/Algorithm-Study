# source : https://leetcode.com/problems/add-to-array-form-of-integer/

class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        return list(str(int(''.join([str(n) for n in num])) + k))