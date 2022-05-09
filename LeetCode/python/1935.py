# source : https://leetcode.com/problems/maximum-number-of-words-you-can-type/

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        result = 0
        
        for word in text.split(' '):
            is_pass = False
            
            for letter in brokenLetters:
                if letter in word:
                    is_pass = True
                    break
            
            if not is_pass:
                result += 1
            
        return result