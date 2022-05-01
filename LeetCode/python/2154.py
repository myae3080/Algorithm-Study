# source : https://leetcode.com/problems/keep-multiplying-found-values-by-two/

class Solution:
    def findFinalValue(self, nums: list[int], original: int) -> int:
        while True:
            if original not in nums:
                return original
            else:
                original *= 2