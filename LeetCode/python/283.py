# source : https://leetcode.com/problems/move-zeroes/

class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_count = nums.count(0)
        nums[:] = [num for num in nums if num != 0]
        [nums.append(0) for _ in range(zero_count)]