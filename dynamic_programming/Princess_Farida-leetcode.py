#   https://www.spoj.com/problems/FARIDA/


def solve(nums):
    length = len(nums)
    dp = [0]*length
    dp[0] = nums[0]
    
    if length > 1:
        dp[1] = max(nums[0], nums[1])
        
        for index in range(2, length):
            dp[index] = max(dp[index-1], dp[index-2]+nums[index])
    
    return dp[-1]


for index in range(int(input())):
    num = int(input())
    if num == 0:
        print(f"Case {index+1}: 0")
    else:
        lis = list(map(int, input().split()))
        ans = solve(lis)
        print(f"Case {index+1}: {ans}")