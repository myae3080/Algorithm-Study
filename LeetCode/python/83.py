# source : https://leetcode.com/problems/remove-duplicates-from-sorted-list/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    # inefficient
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        target = head
        
        while head and head.next:
            if head.next and head.val == head.next.val:
                head.next = head.next.next
            else:
                head = head.next
                
        return target