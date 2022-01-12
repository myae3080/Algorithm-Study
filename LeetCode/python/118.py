# source : https://leetcode.com/problems/pascals-triangle/

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        result = [[1]]
        
        for i in range(2, numRows + 1):
            temp = []
            
            for j in range(i):
                if j == 0:
                    temp.append(1)
                elif j == i - 1:
                    temp.append(1)
                else:
                    temp.append(result[i - 2][j - 1] + result[i - 2][j])
                    
            result.append(temp)
            
        return result