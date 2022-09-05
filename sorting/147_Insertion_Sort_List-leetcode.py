#   https://leetcode.com/problems/insertion-sort-list/



# T.C => 
# S.C => 


from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode(-5001, head)
        prev, curr = head, head.next
        
        while(curr):
            if (curr.val >= prev.val):
                prev = curr
                curr = curr.next
                continue
            
            ptr = dummy
            while(curr.val > ptr.next.val):
                ptr = ptr.next
                
            prev.next = curr.next
            curr.next = ptr.next
            ptr.next = curr
            curr = prev.next
            
        return dummy.next
            

if __name__ == '__main__':
    obj = Solution()
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    
    node4.next = node2
    node2.next = node1
    node1.next = node3
     
    ans = obj.insertionSortList(node4)
    while(ans):
        print(ans.val, end = " => ")
        ans = ans.next