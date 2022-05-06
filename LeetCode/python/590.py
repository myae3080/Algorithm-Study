# source : https://leetcode.com/problems/n-ary-tree-postorder-traversal/

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def postorder(self, root: 'Node') -> list[int]:
        result = []
        
        def dfs(root = root, result = result):
            if root:    
                for child in root.children:
                    dfs(child, result)
                
                result.append(root.val)
                    
        dfs()
        
        return result