# source : https://leetcode.com/problems/contains-duplicate-ii/

class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        nums_dict = {}
        
        for i in range(len(nums)):
            if nums[i] in nums_dict:
                if abs(nums_dict[nums[i]] - i) <= k:
                    return True
                else:
                    nums_dict[nums[i]] = i    
            else:
                nums_dict[nums[i]] = i
        
        return False