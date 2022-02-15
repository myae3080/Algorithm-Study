# source : https://leetcode.com/problems/add-digits/

class Solution:
    def addDigits(self, num: int) -> int:
        nums = list(map(int, str(num)))
        
        while len(nums) > 1:
            nums = list(map(int, str(sum(nums))))
            
        return nums[0]