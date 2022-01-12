# source : https://leetcode.com/problems/reshape-the-matrix/

import itertools

class Solution:
    # inefficient
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        flat_list = list(itertools.chain(*mat))
        
        if r * c != len(flat_list):
            return mat
            
        result = [[0 for j in range(c)] for i in range(r)]
        
        for i in range(r):
            for j in range(c):
                result[i][j] = flat_list.pop(0)
                
        return result