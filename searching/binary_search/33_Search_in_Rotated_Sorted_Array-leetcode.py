#   https://leetcode.com/problems/search-in-rotated-sorted-array/



# T.C => 
# S.C => 


from typing import *


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary1(arr, target):
            length = len(arr)
            left, right = 0, length-1
            
            while(left <= right):
                mid = left + (right-left)//2
                
                if(arr[mid] == target):
                    return mid
                elif(arr[left] <= arr[mid]):
                    if(target >= arr[left] and target <= arr[mid]):
                        right = mid - 1
                    else:
                        left = mid + 1
                else:
                    if(target >= arr[mid] and target <= arr[right]):
                        left = mid + 1
                    else:
                        right = mid - 1
            return -1
        return binary1(nums, target)


if __name__ == '__main__':
    obj = Solution()
    nums = [4,5,6,7,0,1,2]
    target = 8
    ans = obj.search(nums, target)
    print(ans)