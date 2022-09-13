#   https://leetcode.com/problems/valid-sudoku/


from typing import *


# class Solution:
#     def isValidSudoku(self, board: List[List[str]]) -> bool:
#         lookup = [0]*10

#         for row in range(9):
#             for column in range(9):
#                 if board[row][column] == ".":
#                     continue
#                 elif lookup[int(board[row][column])] == 0:
#                     lookup[int(board[row][column])] = 1
#                 else:
#                     return False
#             lookup = [0]*10

#         for column in range(9):
#             for row in range(9):
#                 if board[row][column] == ".":
#                     continue
#                 elif lookup[int(board[row][column])] == 0:
#                     lookup[int(board[row][column])] = 1
#                 else:
#                     return False
#             lookup = [0]*10

#         positions = [[(0,3),(0,3)],[(0,3),(3,6)],[(0,3),(6,9)],[(3,6),(0,3)],[(3,6),(3,6)],[(3,6),(6,9)],[(6,9),(0,3)],[(6,9),(3,6)],[(6,9),(6,9)]]

#         for pos in positions:
#             for row in range(pos[0][0],pos[0][1]):
#                 for column in range(pos[1][0],pos[1][1]):
#                     if board[row][column] == ".":
#                         continue
#                     elif lookup[int(board[row][column])] == 0:
#                         lookup[int(board[row][column])] = 1
#                     else:
#                         return False
#             lookup = [0]*10

#         return True

import collections


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)  # key = (r /3, c /3)
        print(cols, rows, squares)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (
                    board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]
                ):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
        print(cols, rows, squares)
        return True


if __name__ == "__main__":
    obj = Solution()
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]

    ans = obj.isValidSudoku(board)
    print(ans)
