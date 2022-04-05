# source : https://leetcode.com/problems/cells-in-a-range-on-an-excel-sheet/

class Solution:
    def cellsInRange(self, s: str) -> list[str]:
        cells = s.split(':')
        result = []
        
        for i in range(ord(cells[0][0]), ord(cells[1][0]) + 1):
            alphabet = chr(i)
            
            for j in range(int(cells[0][1]), int(cells[1][1]) + 1):
                result.append(alphabet + str(j))
                
        return result
        