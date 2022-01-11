# source : https://leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result = []
        
        for num in nums1:
            if nums2.count(num) > 0:
                result.append(num)
                del nums2[nums2.index(num)]
                
        return result