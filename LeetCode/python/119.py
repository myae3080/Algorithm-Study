# source : https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        pascal = [[1]]
        
        for i in range(1, rowIndex+1):
            row = []
            
            for j in range(i+1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(pascal[i-1][j-1] + pascal[i-1][j])
                    
            pascal.append(row)
            
        return pascal[rowIndex]