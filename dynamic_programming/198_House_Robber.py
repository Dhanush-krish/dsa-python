'''
Choices → what moves/actions can I take? -> rob or leave

State → what information uniquely defines a subproblem? money

Transition → how do smaller states combine into the larger one? max(prev_start , currn + previous -1 )

Base Case → what’s the simplest answer I know immediately? at 1 max is 1, at 2 max is 1,2

Answer → what state(s) give me the final solution? 
'''


class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1: return nums[0]
        if len(nums) == 2: return max(nums[0], nums[1])

        result = [0] * len(nums)

        result[0] = nums[0]
        result[1] = max(nums[0], nums[1])

        for idx in range(2, len(nums)):
            result[idx] = max(result[idx - 1], result[idx - 2] + nums[idx])
        
        return result[-1]
        