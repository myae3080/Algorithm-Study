from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # 트리의 마지막
        if root == None or root.right == None:
            return root
        
        # 2 -> 3 연결
        root.left.next = root.right
        
        # 2 - 3 연결 밑의 노드 5 -> 6 연결
        if root.next != None:
            root.right.next = root.next.left
            
        self.connect(root.left)
        self.connect(root.right)
        
        return root