#   https://leetcode.com/problems/maximum-units-on-a-truck/




from typing import *


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        # boxe_types = sorted(boxTypes, reverse = True, key=lambda x: x[1])   ### consumes more memory and time
        boxTypes.sort(key = lambda x: -x[1])                                  ###less memory and time
        units = 0
        
        for boxes,unit in boxTypes:
            if truckSize == 0:
                return units
            
            if truckSize >= boxes:
                units += (boxes*unit)
                truckSize -= boxes
            else:
                units += (truckSize*unit)
                truckSize = 0    
            
        return units


if __name__ == '__main__':
    obj = Solution()
    boxTypes = [[5,10],[2,5],[4,7],[3,9]]
    truckSize = 10
    ans = obj.maximumUnits(boxTypes, truckSize)
    print(ans)
    
"""
Example 1:

Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
Output: 8
Explanation: There are:
- 1 box of the first type that contains 3 units.
- 2 boxes of the second type that contain 2 units each.
- 3 boxes of the third type that contain 1 unit each.
You can take all the boxes of the first and second types, and one box of the third type.
The total number of units will be = (1 * 3) + (2 * 2) + (1 * 1) = 8.
Example 2:

Input: boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10
Output: 91
"""