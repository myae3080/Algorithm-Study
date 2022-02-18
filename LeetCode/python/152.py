# https://leetcode.com/problems/maximum-product-subarray/

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        first_val = nums[0]
        result, max_val, min_val = first_val, first_val, first_val
        
        for num in nums[1:]:
            max_val, min_val = max(num, max_val * num, min_val * num), min(num, max_val * num, min_val * num)
            result = max(result, max_val)
            
        return result