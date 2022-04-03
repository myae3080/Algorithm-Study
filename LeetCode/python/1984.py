# source : https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/

import sys

class Solution:
    # combinations로 풀려 했으나 time limit
    def minimumDifference(self, nums: list[int], k: int) -> int:
        nums.sort()
        result = sys.maxsize
        
        for i in range(k - 1, len(nums)):
            result = min(result, nums[i] - nums[i - k + 1])
        
        return result