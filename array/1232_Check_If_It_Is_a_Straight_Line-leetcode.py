


from typing import *


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        
        coordinates = [[x,y] for x,y in coordinates if x >=0 and y >= 0]
        
        
        first = coordinates[0]
        diff = abs(first[1]-first[0])
        
        for index in range(1,len(coordinates)):
            cord = coordinates[index]
            prev = coordinates[index-1]
            # print(prev[0],cord[0],prev[1],cord[1],abs(cord[0] - cord[1]),diff)
            # print((prev[0]<=cord[0], prev[1]<=cord[1],abs(cord[0] - cord[1])==diff))
            if not ((prev[0]<=cord[0] and  prev[1]<=cord[1] and abs(cord[0] - cord[1])==diff)):
                return False
        
        return True


if __name__ == '__main__':
    obj = Solution()
    coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
    ans = obj.checkStraightLine(coordinates)
    print(ans)