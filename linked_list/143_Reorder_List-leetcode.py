#   https://leetcode.com/problems/reorder-list/





from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None: return head
        
        ##find the mid
        slow, fast = head, head
        while(fast and fast.next):
            fast = fast.next.next
            slow = slow.next
            
        memory = slow.next
        slow.next = None
        
        ## reverse the 2nd half
        prev = None
        current = memory
        while (current):
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        
        current1 = head
        current2 = prev
        
        while(current1 and current2):
            nxt1 = current1.next
            current1.next = current2
            nxt2 = current2.next
            current1 = nxt1
            current2.next = current1
            current2 = nxt2  
            
        return head


if __name__ == '__main__':
    obj = Solution()
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    
    ans = obj.reorderList(node1)
    while ans:
        print(ans.val, end=" => ")
        ans = ans.next