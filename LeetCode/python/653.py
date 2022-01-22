# source : https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        nums = []
        has_sum = False
        
        def dfs(self, root = root):
            if not root:
                return
            
            nums.append(root.val)
            
            dfs(self, root.left)
            dfs(self, root.right)
            
        dfs(self)
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == k:
                    has_sum = True
                    break
        
        return has_sum