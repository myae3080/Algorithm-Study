# source : https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for i in range(9):
            rows, cols = [], []
            
            for j in range(9):
                row, col = board[i][j], board[j][i]
                
                if row.isdigit():
                    if row not in rows:
                        rows.append(row)
                    else:
                        return False
                    
                if col.isdigit():
                    if col not in cols:
                        cols.append(col)
                    else:
                        return False
                   
        for i in range(2, 9, 3):
            for j in range(9):
                if j == 0 or j == 3 or j == 6:
                    sq = []
                    
                for k in range(i - 2, i + 1):
                    num = board[j][k]
                    
                    if num.isdigit():
                        if num not in sq:
                            sq.append(num)
                        else:
                            return False
                    
                        
        return True