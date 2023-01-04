#   https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/

# TC => 
# SC => 
# 


from typing import *
from collections import Counter

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        freq = Counter(tasks)
        result = 0

        for key, value in freq.items():
            if value == 1:
                return -1
            else:
                result += value//3 + bool(value%3)

        return result 





if __name__ == "__main__":
    obj = Solution()
    tasks = [66,66,63,61,63,63,64,66,66,65,66,65,61,67,68,66,62,67,61,64,66,60,69,66,65,68,63,60,67,62,68,60,66,64,60,60,60,62,66,64,63,65,60,69,63,68,68,69,68,61]
    ans = obj.minimumRounds(tasks)
    print(ans)