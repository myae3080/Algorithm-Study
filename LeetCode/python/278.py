# source : https://leetcode.com/problems/first-bad-version/

class Solution:
    def firstBadVersion(self, n):
        start, end = 0, n
        
        while start < end:
            mid = (start + end) // 2
            # predefined
            temp = isBadVersion(mid)
            
            if not temp:
                start = mid + 1
            else:
                end = mid
                
        return start