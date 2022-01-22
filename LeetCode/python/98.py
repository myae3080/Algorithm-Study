# source : https://leetcode.com/problems/validate-binary-search-tree/

import sys
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        is_valid = True
        
        def isValid(self, tree = root, l = -sys.maxsize, h = sys.maxsize):
            nonlocal is_valid
            
            if tree:
                if tree.val >= h or tree.val <= l:
                    is_valid = False
                    return
            
                # left subtree
                isValid(self, tree.left, l, tree.val)
                # right subtree
                isValid(self, tree.right, tree.val, h)
        
        isValid(self)
        
        return is_valid