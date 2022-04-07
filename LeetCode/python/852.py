# source : https://leetcode.com/problems/peak-index-in-a-mountain-array/

class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        return arr.index(max(arr))