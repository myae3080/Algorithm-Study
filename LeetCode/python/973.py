# source : https://leetcode.com/problems/k-closest-points-to-origin/

class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        result = []
        
        [result.append([(li[0] ** 2) + (li[1] ** 2), li]) for li in points]
        result.sort()
        
        return [result[i][1] for i in range(k)]