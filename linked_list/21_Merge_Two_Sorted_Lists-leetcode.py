#   https://leetcode.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 is None and list2 is None:
            return list1
        elif list1 is None:
            return list2
        elif list2 is None:
            return list1
        
        if list1.val > list2.val:
            head = list2
            sptr = list2
            list2 = list2.next
        else:
            head = list1
            sptr = list1
            list1 = list1.next
            
        while (list1 and list2):
            if list1.val <= list2.val:
                sptr.next = list1
                list1 = list1.next
            else:
                sptr.next = list2
                list2 = list2.next
            sptr = sptr.next
            
        if list2 is None:
            sptr.next = list1
        else:
            sptr.next = list2
        return head
        