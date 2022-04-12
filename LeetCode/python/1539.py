# source : https://leetcode.com/problems/kth-missing-positive-number/

class Solution:
    # 단순 풀이
    # TODO : 다른 방법
    def findKthPositive(self, arr: list[int], k: int) -> int:
        for i in range(1, 2001):
            if i not in arr:
                k -= 1
                
            if k == 0:
                return i