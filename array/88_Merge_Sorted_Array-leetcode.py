#   https://leetcode.com/problems/merge-sorted-array/


from typing import *


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        ptr1 = m-1
        ptr2 = n-1
        ins_pos = n+m-1
        
        def check_pos():
            
            if ptr1 < 0:
                return False
            elif ptr2 < 0:
                return True
            
            return nums1[ptr1] >= nums2[ptr2]
        
        while(ptr1 >=0 or ptr2 >= 0):
            
            if check_pos():
                nums1[ins_pos] = nums1[ptr1]
                ptr1 -= 1
            else:
                nums1[ins_pos] = nums2[ptr2]
                ptr2 -= 1
            
            ins_pos -= 1   
            

if __name__ == '__main__':
    obj = Solution()
    arr1 = [1,2,3,0,0,0]
    m = 3
    arr2 = [2,5,6]
    n = 3
    ans = obj.merge(arr1, m, arr2, n)
    print(arr1)