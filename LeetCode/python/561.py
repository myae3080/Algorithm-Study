# source : https://leetcode.com/problems/array-partition-i/

class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        result = [v for i, v in enumerate(sorted(nums)) if i % 2 == 0]
                
        return sum(result)