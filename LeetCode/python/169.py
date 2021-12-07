# source : https://leetcode.com/problems/majority-element/

class Solution:
    # time limit
    def majorityElement(self, nums: list[int]) -> int:
        for n in nums:
            if nums.count(n) > len(nums) // 2:
                return n
            
    def majorityElement2(self, nums: list[int]) -> int:
        return sorted(nums)[len(nums) // 2]