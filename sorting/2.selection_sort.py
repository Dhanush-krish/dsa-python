


class Solution():
    def selection_sort(self, arr):
        
        length = len(arr)
        
        for index in range(length):
            min_index = index
            
            for index2 in range(index+1, length):
                if arr[index2] < arr[min_index]:
                    min_index = index2
            
            arr[index], arr[min_index] = arr[min_index], arr[index]
        
        return arr
    


# T.C => 
# S.C => 
if __name__ == '__main__':
    obj = Solution()
    arr = [-2, 45, 0, 11, -9]
    ans = obj.selection_sort(arr)
    print(ans)