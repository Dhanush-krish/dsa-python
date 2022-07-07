#   https://leetcode.com/problems/add-two-numbers/




from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummyHead = ListNode(0)
        current, carry = dummyHead, 0
                
        while(l1 or l2 or carry):
            val1 = 0 if l1 is None else l1.val
            val2 = 0 if l2 is None else l2.val
            carry,val = divmod((val1 + val2 + carry),10)
            
            node = ListNode(val)
            current.next = node
            current = current.next
            
            l1 = None if l1 is None else l1.next
            l2 = None if l2 is None else l2.next
        
        return dummyHead.next
            
        
        


if __name__ == '__main__':
    
    node1 = ListNode(9)
    node2 = ListNode(9)
    node3 = ListNode(9)
    node4 = ListNode(9)
    node5 = ListNode(9)
    node6 = ListNode(9)
    node7 = ListNode(9)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    
    node8 = ListNode(9)
    node9 = ListNode(9)
    node10 = ListNode(9)
    node11 = ListNode(9)
    
    node8.next = node9
    node9.next = node10
    node10.next = node11
        
    
    obj = Solution()
    ans = obj.addTwoNumbers(node1, node8)
    
    while(ans):
        print(ans.val, end= " => ")
        ans = ans.next