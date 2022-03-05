# source : https://leetcode.com/problems/n-ary-tree-preorder-traversal/

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def preorder(self, root: 'Node') -> list[int]:
        result = []
        
        def dfs(root = root, result = result):
            if root:
                result.append(root.val)
                
                for child in root.children:
                    dfs(child, result)
        
        dfs()
        
        return result
            