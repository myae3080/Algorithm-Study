# https://leetcode.com/problems/get-maximum-in-generated-array/

class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums = [0] * 101
        nums[1] = 1
        
        for i in range(1, n + 1):
            temp = 2 * i
            
            if 2 <= temp <= n:
                nums[temp] = nums[i]
                
            if 2 <= temp + 1 <= n:
                nums[temp + 1] = nums[i] + nums[i + 1]
                
        return max(nums[:n + 1])