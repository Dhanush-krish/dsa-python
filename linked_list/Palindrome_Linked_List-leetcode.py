#   https://leetcode.com/explore/learn/card/linked-list/219/classic-problems/1209/




from ssl import _create_unverified_context
from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        #find middle
        slow,fast = head,head
        while(fast and fast.next):
            fast = fast.next.next
            slow = slow.next
            
        #reverse the 2nd half
        prev,current = None,slow
        while(current):
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        
        # while(head):
        #     print(head.val, end="-> ")
        #     head = head.next
        # print()   
        # while(prev):
        #     print(prev.val, end="-> ")
        #     prev = prev.next
        # print()
            
        #check for palindrome
        left,right = head,prev
        while left and right:
            if right.val != left.val:
                return False
            left = left.next
            right = right.next
        return True

if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    # node3 = ListNode(3)
    node3 = ListNode(3)
    node4 = ListNode(1)
    # node5 = ListNode()
    # node6 = ListNode()
    # node7 = ListNode()
    node1.next = node2
    node2.next = node3
    node3.next = node4
    # node4.next = node5
    
    obj = Solution()
    ans = obj.isPalindrome(node1)
    print(ans)