


from typing import *


class Solution:
    def isPalindrome(self, s: str) -> bool:
        lis = []
        
        #clean the string
        for element in s:
            if element.isalnum():
                lis.append(element.lower())

        left,right = 0,len(lis)-1
        while (left < right):
            if lis[left] != lis[right]:
                return False
            left += 1
            right -= 1
            
                    
        return True

if __name__ == '__main__':
    obj = Solution()
    s = "0P"
    ans = obj.isPalindrome(s)
    print(ans)
    
"""
Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

"""