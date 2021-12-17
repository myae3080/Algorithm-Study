# source : https://leetcode.com/problems/remove-nth-node-from-end-of-list/

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # runner
        slow = fast = head
        
        # n칸 이동
        for _ in range(n):
            fast = fast.next

        if fast != None:
            # 1칸 씩 이동
            while fast.next:
                slow = slow.next
                fast = fast.next
            
            # 삭제될 다음 노드 위치에 그 뒤의 노드로 대체
            slow.next = slow.next.next
            
            return head
        else:
            slow = slow.next
            
            return slow
