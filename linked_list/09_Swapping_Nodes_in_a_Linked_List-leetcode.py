#   https://leetcode.com/problems/swapping-nodes-in-a-linked-list/




from typing import *

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
        
class Solution:
    def swapNodes(self, head, k):
        
        prev,current = None,head
        index = 1
        
        #reverse the list and get the value
        while(current):
            if index == k:
                temp = current.val
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
            index +=1

        index,prev1,current = 1,None,prev
        while(current):
            if index == k:
                current.val,temp = temp,current.val
            
            nxt = current.next
            current.next = prev1
            prev1 = current
            current = nxt
            index += 1
            
        index,current = 1,prev1
        while(current):
            if index == k:
                current.val = temp
                break
            current = current.next
            index += 1
            
             
        return prev1


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
    ans = obj.swapNodes(node1, 2)
    while ans:
        print(ans.val, end="=> ")
        ans = ans.next