# source : https://leetcode.com/problems/fibonacci-number/

class Solution:
    # tabulation : 24 ms 
    def fib(self, n: int) -> int:
        fibo = [0] * 31
        fibo[1], fibo[2] = 1, 1
        
        if n > 2:
            for i in range(2, n + 1):
                fibo[i] = fibo[i - 1] + fibo[i - 2]
                
        return fibo[n]
    
    # recursion : 672 ms
    def fib2(self, n: int) -> int:
        if n < 2:
            return n
        else:
            return self.fib2(self, n - 1) + self.fib2(self, n - 2)