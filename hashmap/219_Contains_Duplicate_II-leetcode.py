#   https://leetcode.com/problems/contains-duplicate-ii/

# TC => O(n)
# SC => O(n)
# where n is the length of the array


from typing import *


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hmap = {}
        
        for index,val in enumerate(nums):

            if val in hmap  and (index - hmap[val] <= k):
                return True

            hmap[val] = index
        
        return False



if __name__ == "__main__":
    obj = Solution()
    nums = [1,2,3,1,2,3]
    k = 2
    ans = obj.containsNearbyDuplicate(nums, k)
    print(ans)