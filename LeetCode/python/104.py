# source : https://leetcode.com/problems/maximum-depth-of-binary-tree/

from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        depth = 0
        queue = deque([root])
        
        while queue:
            # level 당 +1
            depth += 1
            
            for _ in range(len(queue)):
                temp = queue.popleft()
                
                if temp.left:
                    queue.append(temp.left)
                
                if temp.right:
                    queue.append(temp.right)
        
        return depth