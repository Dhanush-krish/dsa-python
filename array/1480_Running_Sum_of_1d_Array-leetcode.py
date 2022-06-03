#   https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums):
        
        for index in range(1,len(nums)):
            nums[index] = nums[index-1]+nums[index]
            
        return nums
        
        
        
        
if __name__ == '__main__':
    obj = Solution()
    # ip = [1,2,3,4]
    ip = [1]
    ans = obj.runningSum(ip)
    print(ans)