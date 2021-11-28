# source : https://leetcode.com/problems/valid-palindrome/

class Solution:
    # 1 / 52ms
    def isPalindrome(self, s: str) -> bool:
        str_list = []
        
        for c in s:
            if c.isalnum():
                str_list.append(c.lower())
        
        half = len(str_list) // 2
        
        for i in range(half):
            if str_list[i] != str_list[len(str_list) - i - 1]:
                return False

        return True
    
    # 2 / 52ms
    def isPalindrome2(self, s: str) -> bool:
        str_list = []
        
        for c in s:
            if c.isalnum():
                str_list.append(c.lower())
        
        new_str = ''.join(str_list)
        
        return new_str == new_str[::-1]