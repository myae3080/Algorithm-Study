# source : https://leetcode.com/problems/single-number/

class Solution:
    # inefficient
    def singleNumber(self, nums: list[int]) -> int:
        for n in nums:
            if nums.count(n) == 1:
                return n