# source : https://leetcode.com/problems/n-ary-tree-level-order-traversal/

from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node') -> list[list[int]]:
        queue = deque([root])
        result = []
        
        if not root:
            return []
        
        while queue:
            length = len(queue)
            temp = []
            
            for _ in range(length):
                curr = queue.popleft()
                
                temp.append(curr.val)
                
                for child in curr.children:
                    queue.append(child)
            
            result.append(temp)
            
        return result