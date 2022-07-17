


from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        decimal = 0
        
        while(head):
            decimal = (decimal<<1)|head.val
            head = head.next
        
        return decimal


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(0)
    node3 = ListNode(1)
    
    node1.next = node2
    node2.next = node3
    
    obj = Solution()

    ans = obj.getDecimalValue(node1)
    print(ans)
    # while(ans):
    #     print(ans.val, end= " => ")
    #     ans = ans.next