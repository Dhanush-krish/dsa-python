#   https://leetcode.com/problems/two-sum/


class Solution:
    def twoSum(self, nums, target):
        
        lookup = {}
        
        for index,num in enumerate(nums):
            if num in lookup:
                return [index,lookup[num]]
            else:
                lookup[target-num] = index
            print(lookup)

if __name__ == '__main__':
    obj = Solution()
    ip = [2, 7, 11, 15]
    target = 9
    ans = obj.twoSum(ip, target)
    print(ans)