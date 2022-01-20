# source : https://leetcode.com/problems/path-sum/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        isTargetSum = False
        
        def checkTargetSum(self, root, total = targetSum):
            if not root:
                return
            
            total -= root.val
            
            if not root.left and not root.right and total == 0:
                nonlocal isTargetSum
                isTargetSum = True
                
                return 
            else:
                checkTargetSum(self, root.left, total)
                checkTargetSum(self, root.right, total)
               
        checkTargetSum(self, root)
            
        return isTargetSum