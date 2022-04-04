# source : https://leetcode.com/problems/find-target-indices-after-sorting-array/

class Solution:
    # 89ms
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        return [i for i, e in enumerate(sorted(nums)) if e == target]
    
    # 44ms
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        result = []
        
        for i, e in enumerate(sorted(nums)):
            if e == target:
                result.append(i)
                
        return result