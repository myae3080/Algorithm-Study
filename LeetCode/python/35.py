# source : https://leetcode.com/problems/search-insert-position/

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        try:
            return nums.index(target)
        except:
            start, end = 0, len(nums)
            
            while start < end:
                half = (start + end) // 2
                temp = nums[half]
                
                if target < temp:
                    end -= 1
                else:
                    start += 1
                    
            return start