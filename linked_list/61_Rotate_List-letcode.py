#   https://leetcode.com/problems/rotate-list/




from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if head is None: return None
        
        length = 0
        current = head
        while(current):
            length += 1
            current = current.next
            
        k %= length
        till = length-k
            
        ##traverse through n-k
        if k > 0:
            current = head
            while (till>1):
                current = current.next
                till -= 1
            
            newHead = current.next
            current.next = None
            
            curr2 = newHead
            while(curr2.next):
                curr2 = curr2.next
            
            curr2.next = head

            return newHead
        else:
            return head
            


if __name__ == '__main__':

    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    # node4 = ListNode(4)
    # node5 = ListNode(5)
    # node6 = ListNode(6)
    # node7 = ListNode(7)
    
    node1.next = node2
    node2.next = node3
    # node3.next = node4
    # node4.next = node5
    # node5.next = node6
    # node6.next = node7    
    
    obj = Solution()
    ans = obj.rotateRight(node1, 6)
    
    while(ans):
        print(ans.val, end=" => ")
        ans = ans.next