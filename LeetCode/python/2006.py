# source : https://leetcode.com/problems/count-number-of-pairs-with-absolute-difference-k/

class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        count = 0
        
        for i in range(len(nums)):
            curr = nums[i]
            
            for j in range(i, len(nums)):
                if abs(curr - nums[j]) == k:
                    count += 1
                    
        return count
    
    def countKDifference2(self, nums: list[int], k: int) -> int:
        count = 0
        
        for i in range(len(nums)):
            count += nums[i:].count(nums[i] + k)
            count += nums[i:].count(nums[i] - k)
                    
        return count