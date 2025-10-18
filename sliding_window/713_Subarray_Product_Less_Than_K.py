class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        left, result = 0, 0

        product = 1
        for right, val in enumerate(nums):
            product *= val
            
            while(left < len(nums) and product >= k):
                product /= nums[left]
                left += 1
            result += (right - left + 1)
        
        return result if result > 0 else 0