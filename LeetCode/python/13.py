# source : https://leetcode.com/problems/roman-to-integer/

class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        scores = 0
        
        if "IV" in s:
            s = s.replace("IV", "")
            scores += 4
            
        if "IX" in s:
            s = s.replace("IX", "")
            scores += 9
            
        if "XL" in s:
            s = s.replace("XL", "")
            scores += 40
            
        if "XC" in s:
            s = s.replace("XC", "")
            scores += 90
            
        if "CD" in s:
            s = s.replace("CD", "")
            scores += 400
            
        if "CM" in s:
            s= s.replace("CM", "")
            scores += 900
        
        for c in s:
            scores += dic[c]
            
        return scores