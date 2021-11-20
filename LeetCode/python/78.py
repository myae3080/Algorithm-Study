# source : https://leetcode.com/problems/subsets/

from itertools import combinations

class Solution(object):
    def subsets(self, nums):
        result = [[]]

        for i in range(len(nums)):
            for tu in list(combinations(nums, i + 1)):
                result.append(list(tu))

        return result

print(Solution.subsets(Solution, [1, 2, 3]))