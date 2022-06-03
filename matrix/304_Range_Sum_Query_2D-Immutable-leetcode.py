#   https://leetcode.com/problems/range-sum-query-2d-immutable/

# to avoid time limit exceed error create a prefix sum
# compute sum for each row



class NumMatrix:

    def __init__(self, matrix):
        
        self.ps = [[0]*(len(matrix[0])+1) for x in range(len(matrix))]

        for row in range(len(matrix)):
            running_sum = 0
            for column in range(len(matrix[0])):
                running_sum += matrix[row][column]
                self.ps[row][column+1] = running_sum 
        

    def sumRegion(self, row1, col1, row2, col2 ):
        result = 0
        for var in range(row1,row2+1):
            result += ((self.ps[var][col2+1])-(self.ps[var][col1]))
        return result        


if __name__ == '__main__':
    
    matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]
    obj = NumMatrix(matrix)
    ans = obj.sumRegion(2,1,4,3)
    print(ans)
