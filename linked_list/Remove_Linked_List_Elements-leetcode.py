#   https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1207/





from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = prev = ListNode(-1)
        dummy.next = head
        current = head
        
        while (current):
            if current.val == val:
                current = current.next
                prev.next = current
                continue
            prev = current
            current = current.next
        
        return dummy.next if dummy.next else None



if __name__ == '__main__':
    obj = Solution()
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(6) 
    node4 = ListNode(3) 
    node5 = ListNode(4) 
    node6 = ListNode(5) 
    node7 = ListNode(6)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    
    ans = obj.removeElements(node1, 6)
    while ans:
        print(ans.val)
        ans = ans.next