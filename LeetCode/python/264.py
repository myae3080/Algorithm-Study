# source : https://leetcode.com/problems/ugly-number-ii/

class Solution:
    #  inefficient solution
    def nthUglyNumber(self, n: int) -> int:
        result = [1]
        factors = [2, 3, 5]
        start, idx = 0, 0
        
        while start < n:
            start += 1
            temp = [n * result[idx] for n in factors]
            
            for num in temp:
                if num not in result:
                    result.append(num)
            
            result.sort()
            idx += 1
            
        return result[n - 1]