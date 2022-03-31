# source : https://leetcode.com/problems/find-all-duplicates-in-an-array/

from collections import Counter

class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        return [item[0] for item in Counter(nums).items() if item[1] > 1]