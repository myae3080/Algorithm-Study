# source : https://leetcode.com/problems/guess-number-higher-or-lower/

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:
def guess():
    return 0

class Solution:
    def guessNumber(self, n: int) -> int:
        start, end = 1, n
        
        while 1:
            mid = (start + end) // 2
            result = guess(mid)
            
            if result == 1:
                start = mid + 1
            elif result == -1:
                end = mid - 1
            else:
                return mid