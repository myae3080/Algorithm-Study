# source : https://leetcode.com/problems/arithmetic-subarrays/

class Solution:
    def checkArithmeticSubarrays(self, nums: list[int], l: list[int], r: list[int]) -> list[bool]:
        result = []
        
        for i in range(len(l)):
            arr = nums[l[i]:r[i] + 1]
            arr.sort()
            
            if len(set([arr[j] - arr[j - 1] for j in range(1, len(arr))])) == 1:
                result.append(True)
            else:
                result.append(False)
                
        return result