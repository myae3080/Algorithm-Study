# source : https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return ((high - low) // 2) + (0 if low % 2 == 0 and high % 2 == 0 else 1)