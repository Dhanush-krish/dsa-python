#   https://www.codechef.com/START53C/problems/QUEENBL?tab=statement


import io,os,sys
# import math
# from queue import PriorityQueue
# from collections import defaultdict,deque, Counter
# input = sys.stdin.readline
# sys.stdout.write(str(n) + "\n")


def solve(valid):
    # num = int(input())
    r,c = map(int,input().split())
    matrix = [[0 for x in range(1,9)] for y in range(1,9)]
    matrix[r-1][c-1] = 1
    pos1 = [(r-1, c+2),(r+1, c+2),(r+2, c-1),(r-2, c-1)]
    pos2 = [(r-1, c-2),(r+1, c-2),(r+2, c+1),(r-2, c+1)]
    # print(pos1)
    # print(pos2)
    if pos1[0] in valid or pos1[1] in valid:
        if pos1[0] in valid:
            matrix[pos1[0][0]-1][pos1[0][1]-1] = 2
        if pos1[1] in valid:
            matrix[pos1[1][0]-1][pos1[1][1]-1] = 2
        if pos1[2] in valid:
            matrix[pos1[2][0]-1][pos1[2][1]-1] = 2
        elif pos1[3] in valid:
            matrix[pos1[3][0]-1][pos1[3][1]-1] = 2
    else:
        if pos2[0] in valid:
            matrix[pos2[0][0]-1][pos2[0][1]-1] = 2
        if pos2[1] in valid:
            matrix[pos2[1][0]-1][pos2[1][1]-1] = 2
        if pos2[2] in valid:
            matrix[pos2[2][0]-1][pos2[2][1]-1] = 2
        elif pos2[3] in valid:
            matrix[pos2[3][0]-1][pos2[3][1]-1] = 2
        
    
    for val in matrix:
        print(*val)
    
    


T = int(input())
while (T):
    # lis = map(int,input().split())
    # num = int(input())
    valid = [(x,y) for x in range(1,9) for y in range(1,9)]
    solve(valid)
    # output = solve()
    # print(output)
    T -= 1