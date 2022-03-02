# source : https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/

import sys

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: list[list[int]]) -> int:
        mds = []
        
        for point in points:
            temp_x, temp_y = point[0], point[1]
            
            if x == temp_x or y == temp_y:
                mds.append(abs(x - temp_x) + abs(y - temp_y))
            else:
                mds.append(sys.maxsize)
            
        return -1 if len(mds) == mds.count(sys.maxsize) else mds.index(min(mds))