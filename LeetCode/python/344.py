# source : https://leetcode.com/problems/reverse-string/

class Solution:
    def reverseString(self, s: list[str]) -> None:
        s[:] = s[::-1]
        
        # wrong answer / space complexity : O(1)
        # s = s[::-1]