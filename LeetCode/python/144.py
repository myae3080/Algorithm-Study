# source : https://leetcode.com/problems/binary-tree-preorder-traversal/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        result = []
        
        def dfs(self, root):
            if root:
                result.append(root.val)
            
                dfs(self, root.left)
                dfs(self, root.right)
            
        dfs(self, root)
        
        return result