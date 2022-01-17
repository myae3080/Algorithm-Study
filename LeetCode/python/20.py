# source : https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        
        brackets_dict = {
            "(":")",
            "[":"]",
            "{":"}"
        }
        
        stack = []
        
        for c in s:
            if c in brackets_dict:
                stack.append(brackets_dict[c])
            else:
                if len(stack) == 0:
                    return False
                
                if c != stack.pop():
                    return False
                
        if not stack:
            return True
        else:
            return False