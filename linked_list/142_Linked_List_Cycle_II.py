#   https://leetcode.com/problems/linked-list-cycle-ii/




from typing import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

###without constraints
# class Solution:
#     def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
#         lookup = set()
#         node = head
        
#         while(node):
#             if node in lookup:
#                 return node
#             lookup.add(node)
#             node = node.next
            
#         return None

#floyd's     
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        slow , fast = head, head
        
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                break
        
        if fast is None or fast.next is None: return None
        
        slow2=head
        while slow != slow2:
            slow=slow.next
            slow2=slow2.next
        return slow
