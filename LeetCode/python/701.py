# source : https://leetcode.com/problems/insert-into-a-binary-search-tree/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def recursive(self, tree = root):
            if not tree:
                tree = TreeNode(val)
                
                return tree
            
            if tree.val > val:
                tree.left = recursive(self, tree.left)
            else:
                tree.right = recursive(self, tree.right)
                
            return tree
            
        return recursive(self)