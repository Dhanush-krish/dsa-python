#   https://leetcode.com/problems/max-consecutive-ones-iii/




from typing import *


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        zeros,left,result  = 0,0,0
        
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
                
            while(zeros > k):
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            
            result = max(result, right-left+1)
        
        return result


if __name__ == '__main__':
    obj = Solution()
    nums = [1,1,1,0,0,0,1,1,1,1,0]
    k = 2
    ans = obj.longestOnes(nums, k)
    print(ans)