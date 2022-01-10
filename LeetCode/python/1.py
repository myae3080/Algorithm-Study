# source : https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        result = []
        isNotBreak = True
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target and len(result) == 0:
                    result.append(i)
                    result.append(j)
                    
                    isNotBreak = False
                    break
            if isNotBreak == False:
                break
                
        return result