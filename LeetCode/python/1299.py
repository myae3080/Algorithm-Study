# source : https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/

class Solution:
    def replaceElements(self, arr: list[int]) -> list[int]:
        length = len(arr)
        result = []
        
        for i in range(length):
            if i + 1 != length:
                result.append(max(arr[i + 1:]))
            else:
                result.append(-1)
        
        return result