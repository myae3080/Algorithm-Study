# source : https://leetcode.com/problems/subtract-the-product-and-sum-of-digits-of-an-integer/

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        digits = list(map(int, str(n)))
        product = 1
        
        for d in digits:
            product *= d
        
        return product - sum(digits)