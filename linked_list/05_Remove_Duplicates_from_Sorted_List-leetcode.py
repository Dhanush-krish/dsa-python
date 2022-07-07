#   https://leetcode.com/problems/remove-duplicates-from-sorted-list/





from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        current = head
        while current:
            while current.next and current.val == current.next.val:
                current.next = current.next.next
            current = current.next
        
        return head
        



if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(1)
    node3 = ListNode(2)
    node4 = ListNode(3)
    node5 = ListNode(3)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    
    
    obj = Solution()
    ans = obj.deleteDuplicates(node1)
    while ans:
        print(ans.val,"-> ",end= " ")
        ans = ans.next