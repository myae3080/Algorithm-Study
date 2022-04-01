# source : https://leetcode.com/problems/find-first-palindromic-string-in-the-array/

class Solution:
    def isPalindrome(self, word) -> str:
        length = len(word)
        half = length // 2
        is_palindrome = True
        
        for i in range(half):
            if word[i] != word[length - i - 1]:
                is_palindrome = False
                break
                
        return is_palindrome
    
    def firstPalindrome(self, words: list[str]) -> str:
        for word in words:
            if self.isPalindrome(word):
                return word
            
        return ''