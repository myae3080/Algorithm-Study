# source : https://leetcode.com/problems/combinations/

from itertools import combinations

class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        return list(combinations([i + 1 for i in range(n)], k))