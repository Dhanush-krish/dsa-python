class Solution():

    def bubble_sort(self, arr):
        length = len(arr)
        loop_count = 0
        inversion_count = 0

        for iterator in range(length-1):              #length - 1  ---> since list is in sorted order in length-1 iteration so reducing the iterator count

            for index in range(length-1-iterator):      # length-1  ---> accessing current and next element otherwise throws index out of range exception 
                                                    #  - iterator   ---> to decrease limit since elements are already the biggest numbers. 

                if(arr[index] > arr[index + 1]):

                    arr[index] ,arr[index+1] = arr[index+1], arr[index]
                    inversion_count += 1
                # print(arr)

                loop_count += 1

            print(arr)


        print("Number of times iterated - ",loop_count)
        print("Number of times swapped - ",inversion_count)
        return arr


# T(n) =>  O(n**2)
# S(n) => O(1)

class Solution():
    def bubble_sort(self, arr):
        length = len(arr)
        
        for index1 in range(length - 1):
            for index2 in range(length - 1 - index1):
                if arr[index2] > arr[index2 + 1]:
                    arr[index2], arr[index2 + 1] = arr[index2 + 1], arr[index2]
            
        return arr



lis = [7, 4, 5, 2]
print(Solution().bubble_sort(lis))