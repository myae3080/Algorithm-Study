# source : https://leetcode.com/problems/best-sightseeing-pair/

class Solution:
    def maxScoreSightseeingPair(self, values: list[int]) -> int:
        # i_val = values[i] + i
        result, i_val = 0, values[0] + 0
        
        for i in range(1, len(values)):
            curr_val = values[i]
            
            result = max(result, i_val + curr_val - i)
            i_val = max(i_val, curr_val + i)
            
        return result