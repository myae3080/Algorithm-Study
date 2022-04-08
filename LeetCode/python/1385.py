# source : https://leetcode.com/problems/find-the-distance-value-between-two-arrays/

class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        result = 0
        
        for num1 in arr1:
            is_valid = True
            
            for num2 in arr2:
                if abs(num1 - num2) <= d:
                    is_valid = False
                    break
                    
            if is_valid:
                result += 1
                
        return result