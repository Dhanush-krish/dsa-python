

# T.C => 
# S.C => 


from typing import *

class Solution():
    def insertion_sort(self, arr):
        length = len(arr)
        
        for index in range(1, length):
            ref = arr[index]
            prev = index - 1
            
            while(prev >= 0 and ref < arr[prev]):
                arr[prev + 1] = arr[prev] 
                prev -= 1
            
            arr[prev+1] = ref
        
        return arr



if __name__ == '__main__':
    obj = Solution()
    arr = [9, 5, 1, 4, 3]
    ans = obj.insertion_sort(arr)
    print(ans)