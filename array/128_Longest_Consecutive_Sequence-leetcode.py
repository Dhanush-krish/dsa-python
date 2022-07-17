#   https://leetcode.com/problems/longest-consecutive-sequence/




from typing import *


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        uniq = set(nums)
        longest = 0
        
        for value in uniq:
            if value-1 not in uniq:
                curr_length = 1
                curr_val = value
                
                while(curr_val+1 in uniq):
                    curr_length += 1
                    curr_val += 1
                
                longest = max(longest, curr_length)
        return longest
                
        


if __name__ == '__main__':
    obj = Solution()
    lis = [1,2,3,4,5]
    ans = obj.longestConsecutive(lis)
    print(ans)