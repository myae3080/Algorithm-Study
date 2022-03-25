# source : https://leetcode.com/problems/univalued-binary-tree/

from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        num = root.val
        is_uni = True
    
        while queue:
            node = queue.pop()
            
            if node.left:
                if node.left.val != num:
                    is_uni = False
                    break
                else:
                    queue.append(node.left)
                
            if node.right:
                if node.right.val != num:
                    is_uni = False
                    break
                else:
                    queue.append(node.right)
                
        return is_uni