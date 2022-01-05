# source : https://leetcode.com/problems/permutations-ii/

from itertools import permutations
 
class Solution:
    def permuteUnique(self, nums: list[int]) -> list[list[int]]:
        return list(set(permutations(nums, len(nums))))