#   https://leetcode.com/problems/remove-nth-node-from-end-of-list/




from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

class Solution:
    def removeNthFromEnd(self, head, n: int):
        
        ##reversr the linked list
        prev, current = None, head
        while(current):
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        
        newHead, current = prev, prev
        dummyHead = ListNode(-1)
        prev = dummyHead
        dummyHead.next = newHead
        
        while(n > 1 and current):
            prev.next = current
            prev = prev.next
            current = current.next
            n-=1
        
        prev.next = current.next
        
        head = None if dummyHead.next is None else dummyHead.next

        current = head
        prev = None
        
        while(current):
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        return prev
        


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    obj = Solution()
    ans = obj.removeNthFromEnd(node1, 3)
    
    while(ans):
        print(ans.val, end="=> ")
        ans = ans.next