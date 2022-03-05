# source : https://leetcode.com/problems/sum-of-all-odd-length-subarrays/

class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        result = 0
        length = len(arr)
        odd = 1
        
        while odd <= length:
            for i in range(length):
                end = i + odd

                if end <= length:
                    result += sum(arr[i:end])
                
            odd += 2
            
        return result