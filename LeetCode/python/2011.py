# https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

class Solution:
    def finalValueAfterOperations(self, operations: list[str]) -> int:
        result = 0
        
        for s in operations:
            if s.find("-") >= 0:
                result -= 1
            else:
                result += 1
                
        return result