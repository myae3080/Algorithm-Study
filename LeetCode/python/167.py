# source : https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

class Solution:
    def twoSum(self, numbers:list[int], target: int) ->list[int]:
        start, end = 0, len(numbers) - 1
        
        while start < end:
            num = numbers[start] + numbers[end]
            
            if num == target:
                return [start + 1, end + 1]
            elif num > target:
                end -= 1
            else:
                start += 1