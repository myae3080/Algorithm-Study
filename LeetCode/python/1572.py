# source : https://leetcode.com/problems/matrix-diagonal-sum/

class Solution:
    def diagonalSum(self, mat: list[list[int]]) -> int:
        length = len(mat[0])
        result, idx = 0, 0
        
        for i in range(length):
            result += mat[idx][i]
            idx += 1
                
        for i in range(length):
            result += mat[i][idx - 1]
            idx -= 1
        
        # 중복값 제거
        if length % 2 == 1:
            center = length // 2
            result -= mat[center][center]
            
        return result