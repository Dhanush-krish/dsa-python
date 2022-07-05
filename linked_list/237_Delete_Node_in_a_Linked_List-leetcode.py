#   https://leetcode.com/problems/delete-node-in-a-linked-list/




from typing import *


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        # change the value to next node and remove the next node
        #  coz we don't know the previous node
        
        node.val = node.next.val
        node.next = node.next.next


if __name__ == '__main__':
    obj = Solution()
    ans = obj.
    print(ans)