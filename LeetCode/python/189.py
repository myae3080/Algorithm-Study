# source : https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        
        if length < 3:
            nums[:] = nums[k % length:] + nums[:k % length]
        else:
            nums[:] = nums[length - k:] + nums[:length - k]