# source : https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        binary = []
        result, idx = 0, 0
        
        while head:
            binary.append(head.val)
            head = head.next
            
        for b in binary[::-1]:
            result += b * (2 ** idx)
            idx += 1
            
        return result
        
        