#   https://leetcode.com/explore/learn/card/linked-list/214/two-pointer-technique/1212/

from typing import *


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow,fast = head,head
        
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            if slow == fast :
                return True
        
        return False


if __name__ == '__main__':
    obj = Solution()
    ans = obj.hasCycle()
    print(ans)