# source : https://leetcode.com/problems/next-greater-element-ii/

class Solution:
    # time limit은 피했으나, 너무 비효율적...
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        length = len(nums)
        result = [-1] * length
        
        for i in range(length):
            curr = nums[i]
            
            for j in range(i + 1, i + length):
                if nums[j % length] > curr:
                    result[i] = nums[j % length]
                    break
                
        return result