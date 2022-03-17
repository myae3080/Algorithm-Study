# source : https://leetcode.com/problems/sqrtx/

import math

class Solution:
    def mySqrt(self, x: int) -> int:
        return math.trunc(x ** 0.5)