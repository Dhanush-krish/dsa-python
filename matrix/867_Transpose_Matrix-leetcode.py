#   https://leetcode.com/problems/transpose-matrix/

class Solution:
    def transpose(self, matrix):
        
        transposed = []
        for column in range(len(matrix[0])):
            temp = []
            for row in range(len(matrix)):
                temp.append(matrix[row][column])
            transposed.append(temp)

        return transposed
    

if __name__ == '__main__':
    obj = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    # matrix = [[1,2,3],[4,5,6]]
    ans = obj.transpose(matrix)
    print(ans)