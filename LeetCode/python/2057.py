# source : https://leetcode.com/problems/smallest-index-with-equal-value/

class Solution:
    def smallestEqual(self, nums: list[int]) -> int:
        try:
            return [i % 10 == nums[i] for i in range(len(nums))].index(1)
        except:
            return -1