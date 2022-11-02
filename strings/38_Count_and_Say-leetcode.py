#   https://leetcode.com/problems/count-and-say/

# TC => 
# SC => 


from typing import *


class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"

        for _ in range(1, n):
            temp = ""
            ptr1 = 0

            for ptr2 in range(len(result)):
                if result[ptr2] != result[ptr1]:
                    temp += str(ptr2 - ptr1) + result[ptr1]
                    ptr1 = ptr2
                    
            temp += str(ptr2 - ptr1 + 1) + result[ptr1]

            result = temp

        return result



if __name__ == "__main__":
    obj = Solution()
    ans = obj.countAndSay(10)
    print(ans)