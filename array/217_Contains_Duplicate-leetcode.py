#   https://leetcode.com/problems/contains-duplicate/


class Solution(object):
    def containsDuplicate(self, nums):
        lookup = set()
        
        for val in nums:
            if val in lookup:
                return True
            else:
                lookup.add(val)

        return False
    
if __name__ == '__main__':
    obj = Solution()
    ip = [1, 2, 3, 4, 5, 1]
    ans = obj.containsDuplicate()
    print(ans)