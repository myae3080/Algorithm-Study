# source : https://leetcode.com/problems/binary-tree-level-order-traversal/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        if not root:
            return []
        
        queue = [root]
        result = []
        
        while queue:
            li = []
            
            for _ in range(len(queue)):
                node = queue.pop(0)
                
                li.append(node.val)
                
                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
                    
            result.append(li)
                
        return result