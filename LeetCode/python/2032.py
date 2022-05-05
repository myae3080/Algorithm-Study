# source : https://leetcode.com/problems/two-out-of-three/

class Solution:
    def twoOutOfThree(self, nums1: list[int], nums2: list[int], nums3: list[int]) -> list[int]:
        nums = {}
        
        for num in set(nums1):
            if num not in nums:
                nums[num] = 1
            else:
                nums[num] += 1
        
        for num in set(nums2):
            if num not in nums:
                nums[num] = 1
            else:
                nums[num] += 1
                
        for num in set(nums3):
            if num not in nums:
                nums[num] = 1
            else:
                nums[num] += 1
                
        return [n for n, v in nums.items() if v >= 2]