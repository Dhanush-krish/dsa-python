#   https://leetcode.com/problems/linked-list-cycle-ii/




from typing import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        lookup = set()
        node = head
        
        while(node):
            if node in lookup:
                return node
            lookup.add(node)
            node = node.next
            
        return None



if __name__ == '__main__':
    obj = Solution()
    ans = obj.
    print(ans)