# source : https://leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution:
    # 68ms
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result = []
        
        for num in nums1:
            if nums2.count(num) > 0:
                result.append(num)
                del nums2[nums2.index(num)]
                
        return result
    
    # 48ms
    def intersect2(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result = []
        dic = {}
        
        for n in nums1:
            if n not in dic:
                dic[n] = 1
            else:
                dic[n] += 1
                
        for n in nums2:
            if n in dic and dic[n] > 0:
                result.append(n)
                dic[n] -= 1
                
        return result