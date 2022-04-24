# source : https://leetcode.com/problems/range-sum-of-bst/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
from collections import deque

class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        queue = deque([root])
        result = 0
        
        while queue:
            node = queue.pop()
            
            if high >= node.val >= low:
                result += node.val
                
            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)
        
        return result