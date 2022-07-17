#   https://leetcode.com/problems/top-k-frequent-elements/




from typing import *
from collections import Counter

# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         sort = sorted(Counter(nums).items(),key = lambda x:-x[1])
#         return [sort[x][0] for x in range(k)]
    
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]
        print(count, freq)
        
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)
            
        print(count, freq)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

if __name__ == '__main__':
    obj = Solution()
    nums = [1,1,1,2,2,3,3,3,3,0,0,0,0]
    k = 2
    ans = obj.topKFrequent(nums, k)
    print(ans)