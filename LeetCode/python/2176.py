# source : https://leetcode.com/problems/count-equal-and-divisible-pairs-in-an-array/

class Solution:
    def countPairs(self, nums: list[int], k: int) -> int:
        length = len(nums)
        count = 0
        
        for i in range(length):
            num1 = nums[i]
            
            for j in range(i + 1, length):
                num2 = nums[j]
                
                if (num1 == num2) and ((i * j) % k == 0):
                    count += 1
        
        return count