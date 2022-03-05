# source : https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result = []
        
        for num in nums1:
            is_found = False

            if nums2.index(num) >= 0:
                for n in nums2[nums2.index(num):]:
                    if n > num:
                        result.append(n)
                        is_found = True
                        break
                        
                if not is_found:
                    result.append(-1)
        
        return result