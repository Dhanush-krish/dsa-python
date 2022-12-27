#   https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks/

# TC => O(n)
# SC => O(n)
# where n is the length of the capacity or rocks


from typing import *


class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        filled = 0
        rem = []

        for idx in range(len(capacity)):
            if capacity[idx] == rocks[idx]:
                filled += 1
            else:
                rem.append(capacity[idx] - rocks[idx])
        
        rem.sort()

        while(rem and additionalRocks and rem[0] <= additionalRocks):
            value = rem.pop(0)
            additionalRocks -= value 
            filled += 1

        return filled


if __name__ == "__main__":
    obj = Solution()
    capacity = [2,3,4,5]
    rocks = [1,2,4,4]
    additionalRocks = 2
    ans = obj.maximumBags(capacity, rocks, additionalRocks)
    print(ans)