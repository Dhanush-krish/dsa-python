#   https://www.codechef.com/JULY222D/problems/SUMOFPROD1



import io,os,sys
# import math
# from queue import PriorityQueue
# from collections import defaultdict,deque, Counter
# input = sys.stdin.readline
# sys.stdout.write(str(n) + "\n")


def solve():
    # num = int(input())
    # lis = list(map(int,input().split()))
    lis = [1,0,1]
    
    result = 0
    c_ones = 0
    for val in lis:
        if val:
            c_ones += 1
            continue
        result += ((c_ones*(c_ones+1))//2)
        c_ones = 0
    result += ((c_ones*(c_ones+1))//2)
    print(result)
    


solve()
# T = int(input())
# while (T):
#     # lis = map(int,input().split())
#     # num = int(input())
#     solve()
#     # output = solve()
#     # print(output)
#     T -= 1