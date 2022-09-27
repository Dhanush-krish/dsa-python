for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    
    for index in range(n):
        if nums[index] >= 0:
            nums[index] = (nums[index]+1)*-1
    
    if n%2 == 1:
        nums.sort()
        nums[0] = -1*(nums[0]+1)
    
    result = 1
    for val in nums:
        result *= val
    
    print(result%((10**9)+7))