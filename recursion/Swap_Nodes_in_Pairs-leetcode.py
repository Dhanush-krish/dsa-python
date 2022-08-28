#   https://leetcode.com/explore/learn/card/recursion-i/250/principle-of-recursion/1681/




from typing import *


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def swap(node):
            if node is None or node.next is None: return None
            
            node.val, node.next.val = node.next.val, node.val   
            swap(node.next.next)
        
        swap(head)
        
        return head


if __name__ == '__main__':
    obj = Solution()
    
    node1 = ListNode(1)
    node2 = ListNode(2)
    # node3 = ListNode(3)
    # node4 = ListNode(4)
    
    node1.next = node2
    # node2.next = node3
    # node3.next = node4
    
    ans = obj.swapPairs(node1)
    
    while(ans):
        print(ans.val, end=" => ")
        ans = ans.next