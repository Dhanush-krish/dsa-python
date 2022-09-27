#       https://leetcode.com/problems/utf-8-validation/


# T.C =>
# S.C =>


from typing import *


class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        LEN = len(data)
        binary = [bin(x)[2:] for x in data]
        print(binary)

        right = 0

        while right < LEN:
            bytes_ = 0
            while bytes_ < len(binary[0]) and binary[0][bytes_] == "1":
                bytes_ += 1
            print(bytes_)
            left = right + 1
            right += bytes_

            while left < LEN and left < right:
                if binary[left][:2] != "10" or len(binary[left]) != 8:
                    return False
                left += 1
        return True


if __name__ == "__main__":
    obj = Solution()
    data = [255]
    ans = obj.validUtf8(data)
    print(ans)

"""
Example 1:

Input: data = [197,130,1]
Output: true
Explanation: data represents the octet sequence: 11000101 10000010 00000001.
It is a valid utf-8 encoding for a 2-bytes character followed by a 1-byte character.
Example 2:

Input: data = [235,140,4]
Output: false
Explanation: data represented the octet sequence: 11101011 10001100 00000100.
The first 3 bits are all one's and the 4th bit is 0 means it is a 3-bytes character.
The next byte is a continuation byte which starts with 10 and that's correct.
But the second continuation byte does not start with 10, so it is invalid.
"""
