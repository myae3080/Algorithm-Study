# source : https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/

class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        result = []
        
        [result.append((num, str(bin(num)[2:]).count('1'))) for num in arr]
        result.sort(key=lambda tu: (tu[1], tu[0]))
        
        return [li[0] for li in result]