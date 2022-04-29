# source : https://leetcode.com/problems/replace-all-digits-with-characters/

class Solution:
    def replaceDigits(self, s: str) -> str:
        result = ''
        
        for i in range(len(s)):
            char = s[i]
            
            if char.isdigit():
                result += chr(ord(s[i - 1]) + int(char))
            else:
                result += char
                
        return result