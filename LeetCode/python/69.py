# source : https://leetcode.com/problems/sqrtx/

import math

class Solution:
    # 24ms
    def mySqrt(self, x: int) -> int:
        return math.trunc(x ** 0.5)
    
    # 40ms
    def mySqrt2(self, x: int) -> int:
        start, end = 0, math.ceil(x / 2)
        result = 0
        
        while start <= end:
            mid = (start + end) // 2
            sqr = mid * mid

            if sqr == x:
                result = mid
                break
            elif sqr < x:
                start = mid + 1
                
                result = mid
            else:
                end = mid - 1
                
        return result