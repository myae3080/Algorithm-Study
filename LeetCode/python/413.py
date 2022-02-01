# source : https://leetcode.com/problems/arithmetic-slices/

class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        length = len(nums)
        
        # exception
        if length < 3:
            return 0
        
        # logic
        result, pointer = 0, 1
        diff = nums[1] - nums[0]
        
        for i in range(2, length):
            curr_diff = nums[i] - nums[i-1]
            
            if curr_diff == diff:
                result += pointer
                pointer += 1
            else:
                diff = curr_diff
                pointer = 1
                
        return result