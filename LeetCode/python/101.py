# source : https://leetcode.com/problems/symmetric-tree/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def checkSymmetric(self, left, right):
            if not left and not right:
                return True
            else:
                if not left or not right:
                    return left == right
                
                if left.val == right.val:
                    return checkSymmetric(self, left.left, right.right) and checkSymmetric(self, left.right, right.left)
                    
                return False
            
        return checkSymmetric(self, root.left, root.right)