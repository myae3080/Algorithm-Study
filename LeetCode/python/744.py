# source : https://leetcode.com/problems/find-smallest-letter-greater-than-target/

class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        result = None
        
        if ord(letters[-1]) > ord(target):
            for letter in letters:
                if ord(letter) > ord(target):
                    result = letter
                    break
        else:
            result = letters[0]
            
        return result