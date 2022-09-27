"""
n = 3
arr[] = {0900, 0940, 0950, 1100, 1500, 1800}
dep[] = {0910, 1200, 1120, 1130, 1900, 2000}
"""

# trains = int(input())
# arr = list(map(int, input().split()))
# depart = list(map(int, input().split()))
arr = [900, 940, 950, 1100, 1500, 1800]
depart = [910, 1200, 1120, 1130, 1900, 2000]  #[910, 1120, 1130, 1200, 1900, 2000]
arr.sort()
depart.sort()
length = len(arr)
max_platform,curr_platform = 1,1
i,j = 1,0

while(i < length and j < length):
    if (arr[i] <= depart[j]):
        i += 1
        curr_platform += 1
    else:
        curr_platform -= 1
        j += 1
    
    max_platform = max(max_platform, curr_platform)
print(max_platform)
            

# schedule =list(zip(arr,depart))
# schedule.sort()
# max_platform ,current_platform = 0, 0
# left = 0
# for right,time in enumerate(schedule):
#     while(not (time[0] < schedule[left][1])):
#         left += 1
#     max_platform = max(max_platform, right-left+1)
# print(max_platform)