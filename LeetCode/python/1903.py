# source : https://leetcode.com/problems/largest-odd-number-in-string/

class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num), 0, -1):
            if int(num[i - 1]) % 2 != 0:
                return num[:i]

        return ""