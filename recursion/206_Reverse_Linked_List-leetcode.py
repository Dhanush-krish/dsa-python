#   https://leetcode.com/problems/reverse-linked-list/




from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# class Solution:
#     def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         if head is None: return None
#         nxt = head.next
#         print(nxt.val, end=" => ")
#         head.next = self.reverseList(head.next)
        
#         return nxt

if __name__ == '__main__':
    
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    
    # obj = Solution()
    # ans = obj.reverseList(node1)
    
    while(node1):
        print(node1.val, end=" => ")
        node1 = node1.next