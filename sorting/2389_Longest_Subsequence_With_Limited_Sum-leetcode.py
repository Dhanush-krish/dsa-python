#   https://leetcode.com/problems/longest-subsequence-with-limited-sum/


# TC => O(n*n) where n is the legth of the nums 
# SC => O(m) where m is the the number of queries
# 


from typing import *


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        LEN = len(nums)
        result = []

        for index in range(1, LEN):
            nums[index] = nums[index-1] + nums[index]
        
        for query in queries:
            for index, value in enumerate(nums):
                if value > query:
                    result.append(index)
                    break
                elif value == query:
                    result.append(index+1)
                    break
            else:
                result.append(LEN)
        
        return result
                



if __name__ == "__main__":
    obj = Solution()
    nums = [2,3,4,5]
    queries = [1]
    ans = obj.answerQueries(nums, queries)
    print(ans)