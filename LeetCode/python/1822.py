# source : https://leetcode.com/problems/sign-of-the-product-of-an-array/

class Solution:
    def arraySign(self, nums: list[int]) -> int:
        if nums.count(0):
            return 0
        
        neg_count = 0
        
        for num in nums:
            if num < 0:
                neg_count += 1
                
        if neg_count % 2 == 0:
            return 1
        else:
            return -1