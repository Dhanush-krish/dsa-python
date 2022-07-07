#   https://leetcode.com/problems/swap-nodes-in-pairs/





from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        
        dummyHead = prev = ListNode(0)
        dummyHead.next = head
        
        while (current and current.next):
            nxt1 = current.next
            nxt2 = current.next.next
            current.next.next = current
            current.next = nxt2
            current = current.next
            prev.next = nxt1
            prev = prev.next.next
            
        
        return None if dummyHead.next is None else dummyHead.next
        


if __name__ == '__main__':

    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node6 = ListNode(6)
    node7 = ListNode(7)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    obj = Solution()
    ans = obj.swapPairs(node1)
    # print(ans)
    while(ans):
        print(ans.val, end= " => ")
        ans = ans.next