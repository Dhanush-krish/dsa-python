# https://leetcode.com/problems/keys-and-rooms/description/

# TC => O(n)
# SC => O(n)
# where n is the number of rooms


from typing import *


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        lookup = set()
        visit = [0]

        while(visit):
            key = visit.pop()
            lookup.add(key)

            for explore in rooms[key]:
                if explore not in lookup:
                    visit.append(explore)

        return len(lookup) == len(rooms)



if __name__ == "__main__":
    obj = Solution()
    rooms = [[1,3],[3,0,1],[2],[0]]
    ans = obj.canVisitAllRooms(rooms)
    print(ans)
    