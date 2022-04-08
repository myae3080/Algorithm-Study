# source : https://leetcode.com/problems/valid-perfect-square/

class Solution:
    # 47ms
    def isPerfectSquare(self, num: int) -> bool:
        sqrt = num ** 0.5
        is_perfect_square = False
        
        if sqrt == int(sqrt):
            is_perfect_square = True
                
        return is_perfect_square
    
    # 54ms
    def isPerfectSquare2(self, num: int) -> bool:
        start, end = 0, 1 if num == 1 else num // 2
        is_perfect_square = False
        
        while start <= end:
            mid = (start + end) // 2
            sqrt = mid ** 2
            
            if sqrt == num:
                is_perfect_square = True
                break
            elif sqrt > num:
                end = mid - 1
            else:
                start = mid + 1
                
        return is_perfect_square