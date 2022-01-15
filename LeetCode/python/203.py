# source : https://leetcode.com/problems/remove-linked-list-elements/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy, dummy.next = ListNode(), head
        new = dummy
        
        while dummy and dummy.next:
            if dummy.next.val == val:
                dummy.next = dummy.next.next
            else:
                dummy = dummy.next
            
        return new.next