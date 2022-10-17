

from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode(0, head)
        fast, slow = dummy, dummy.next
        prev = dummy

        while (fast.next and fast.next.next):
            fast = fast.next.next
            prev = slow
            slow = slow.next
        
        prev.next = slow.next

        return dummy.next if dummy.next else None




if __name__ == "__main__":
    obj = Solution()
    
    node1 = ListNode(1)
    node2 = ListNode(3)
    node3 = ListNode(4)
    node4 = ListNode(7)
    node5 = ListNode(1)
    node6 = ListNode(2)
    node7 = ListNode(6)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7

    ans = obj.deleteMiddle(node1)

    while (ans):
        print(ans.val)
        ans = ans.next 

