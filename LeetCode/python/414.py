# source : https://leetcode.com/problems/third-maximum-number/

class Solution:
    def thirdMax(self, nums: list[int]) -> int:
        nums_set = sorted(set(nums), reverse = True)
        
        if len(nums_set) >= 3:
            return nums_set[2]
        else:
            return nums_set[0]