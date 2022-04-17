# source : https://leetcode.com/problems/count-good-triplets/

class Solution:
    def countGoodTriplets(self, arr: list[int], a: int, b: int, c: int) -> int:
        length = len(arr)
        count = 0
        
        for i in range(length):
            num1 = arr[i]
            
            for j in range(i + 1, length):
                num2 = arr[j]
                
                if abs(num1 - num2) <= a:
                    for k in range(j + 1, length):
                        num3 = arr[k]
                        
                        if abs(num2 - num3) <= b and abs(num1 - num3) <= c:
                            count += 1
                            
        return count