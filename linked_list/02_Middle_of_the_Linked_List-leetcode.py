#   https://leetcode.com/problems/middle-of-the-linked-list/


from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = ListNode(0)
        fast.next = head
        slow = head
        
        while(fast.next and fast.next.next):
            slow = slow.next
            fast = fast.next.next
            
        return slow
        