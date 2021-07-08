'''
source
https://leetcode.com/problems/palindrome-linked-list/
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        target_list = []
        
        # list 변환
        while head:
            target_list.append(head.val)
            head = head.next

        idx = len(target_list) // 2

        for i in range(idx):
            if target_list.pop(0) != target_list.pop():
                return False

        return True

testList = ListNode(1, ListNode(2, ListNode(2, ListNode(1))))

print(Solution.isPalindrome(Solution, testList))