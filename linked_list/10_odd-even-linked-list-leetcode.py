#   https://leetcode.com/problems/odd-even-linked-list/




from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def oddEvenList(self, head):
        
        if head is None: return None
        
        oddHead, oddPtr = head, head
        evenHead, evenPtr = oddHead.next, oddHead.next
        
        while(evenPtr and evenPtr.next):
            
            oddPtr.next = evenPtr.next
            oddPtr = oddPtr.next
            
            evenPtr.next = oddPtr.next
            evenPtr = evenPtr.next
        
        oddPtr.next = evenHead
        
        return oddHead 

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
    ans = obj.oddEvenList(node1)
    
    while(ans):
        print(ans.val, end="=> ")
        ans = ans.next