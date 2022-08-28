#   https://leetcode.com/problems/plus-one/




from typing import *



class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        carry = 0
        length = len(digits)-1
        for index in range(length, -1, -1):
            if index == length:
                carry = (digits[index]+1)//10
                digits[index] = (digits[index]+1)%10
            else:
                new_carry = (digits[index]+carry)//10
                digits[index] = (digits[index]+carry)%10
                carry = new_carry
                
                            
        if carry:
            digits.insert(0, 1)
            
        return digits


if __name__ == '__main__':
    obj = Solution()
    digits = [8,9,9,9]
    ans = obj.plusOne(digits)
    print(ans)
    
    
"""
Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
"""