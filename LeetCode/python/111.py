# source : https://leetcode.com/problems/minimum-depth-of-binary-tree/

from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        # 예외처리
        if not root:
            return 0
        
        queue = deque([root])
        depth = 0
        
        while queue:
            is_leaf = False
            depth += 1
            
            for _ in range(len(queue)):
                node = queue.popleft()
                
                if not node.left and not node.right:
                    is_leaf = True
                    break
                else:
                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)
            
            if is_leaf:
                break
                
        return depth