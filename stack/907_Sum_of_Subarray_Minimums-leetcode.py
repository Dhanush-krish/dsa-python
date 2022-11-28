#   https://leetcode.com/problems/sum-of-subarray-minimums/


# TC => 
# SC => 


from typing import *


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        result = sum(arr)

        for idx1 in range(len(arr)):
            mini = arr[idx1]
            for idx2 in range(idx1 + 1, len(arr)):
                mini = min(mini, arr[idx2])
                result += mini
            #     print([idx1, idx2+1], result, end = " ")
            # print()
        
        return result % ((10**9)+7)




if __name__ == "__main__":
    obj = Solution()
    arr = [3,1,2,4]
    ans = obj.sumSubarrayMins(arr)
    print(ans)