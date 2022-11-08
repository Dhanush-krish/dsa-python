#   https://leetcode.com/problems/make-the-string-great/

# TC => O(n)
# SC => O(n)
# where n is the length of the string


from typing import *


class Solution:
    def makeGood(self, s: str) -> str:
        stack = [s[0]]

        for val in s[1:]:

            if stack and abs(ord(stack[-1]) - ord(val)) - 32 == 0:
                stack.pop()
            else:
                stack.append(val)


        return "".join(stack)



if __name__ == "__main__":
    obj = Solution()
    s = "s"
    ans = obj.makeGood(s)
    print(ans)