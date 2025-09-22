class Solution:

    def dp(self, nums):
        n = len(nums)

        if n == 1: return nums[0]
        if n == 2: return max(nums[0], nums[1])

        result = [0] * n

        result[0], result[1] = nums[0], max(nums[0], nums[1])

        for idx in range(2, n ):
            result[idx] = max(result[idx - 1], result[idx - 2] + nums[idx])

        return result[n-1]

    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1: return nums[0]
        if n == 2: return max(nums[0], nums[1])
        
        return max(self.dp(nums[1:]), self.dp(nums[:-1]))
        
