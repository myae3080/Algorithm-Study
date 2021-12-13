# source : https://leetcode.com/problems/binary-search/

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        try:
            answer = nums.index(target)
        except:
            return -1
        
        return answer