# source : https://leetcode.com/problems/deepest-leaves-sum/

from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        result = []
        
        while queue:
            temp = 0
            
            for _ in range(len(queue)):
                node = queue.popleft()
                
                temp += node.val
                
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
            result.append(temp)
                    
        return result[-1]