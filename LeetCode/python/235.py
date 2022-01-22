# source : https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        max_val = max(p.val, q.val)
        min_val = min(p.val, q.val)
        
        queue = [root]
        result = None
        
        while queue:
            node = queue.pop()
            
            if min_val <= node.val <= max_val:
                result = TreeNode(node.val)
                break
            else:
                if node.val > max_val:
                    queue.append(node.left)
                else:
                    queue.append(node.right)
                    
        return result