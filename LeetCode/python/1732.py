# source : https://leetcode.com/problems/find-the-highest-altitude/

class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        length = len(gain)
        altitudes = [0] * (length + 1) 
        
        for i in range(length):
            altitudes[i + 1] = altitudes[i] + gain[i]
            
        return max(altitudes)