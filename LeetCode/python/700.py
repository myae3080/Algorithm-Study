# source : https://leetcode.com/problems/search-in-a-binary-search-tree/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        queue = [root]
        result = None
        
        while queue:
            node = queue.pop()
            
            if node:
                if node.val == val:
                    result = node
                    break
                else:
                    queue.append(node.left)
                    queue.append(node.right)
                
        return result