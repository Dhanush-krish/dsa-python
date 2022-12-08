
import io,os,sys
# import math
# from queue import PriorityQueue
# from collections import defaultdict,deque, Counter
# input = sys.stdin.readline
# sys.stdout.write(str(n) + "\n")


def solve():
    hmap = {}
    LEN = 3
    string = "abc"
    idx1  = 0

    while(idx1 < LEN):

        idx2 = idx1+1
        while(idx2 < LEN and string[idx2] == string[idx1]):

            idx2 += 1
        temp = string[idx1: idx2]
        hmap[(temp, idx2 - idx1 )] = 1 + hmap.get((temp, idx2 - idx1 ), 0)
        idx1 = idx2 
    

    result1 = result2 = 0
    for key, value in hmap.items():
        if value  > 1:
            result1 = max(result1, key[1])

        result2 = max(result2, key[1])
    
    print(max((result2-1), result1))
solve()
# T = int(input())
# while (T):
#     # lis = map(int,input().split())
#     # num = int(input())
#     solve()
#     # output = solve()
#     # print(output)
#     T -= 1