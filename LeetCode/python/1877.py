# source : https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/

class Solution:
    def minPairSum(self, nums: list[int]) -> int:
        nums.sort()
        
        length = len(nums)
        half = length // 2
        
        return max([nums[i] + nums[length - i - 1] for i in range(half)])