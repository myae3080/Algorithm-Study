# source : https://leetcode.com/problems/balanced-binary-tree/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:        
        def dfs(root = root):
            if not root:
                return 1
            
            left = dfs(root.left)
            right = dfs(root.right)
            
            print(root.val, left, right)
            
            if abs(left - right) > 1 or not left or not right:
                return 0
            
            return max(left, right) + 1
            
        return dfs()