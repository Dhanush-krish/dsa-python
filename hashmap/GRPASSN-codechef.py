import io,os,sys
# import math
# from queue import PriorityQueue
from collections import defaultdict,deque,Counter
# input = sys.stdin.readline
# sys.stdout.write(str(n) + "\n")


def solve():
    num = int(input())
    lis = list(map(int,input().split()))
    
    for key,value in Counter(lis).items():
        if value%key != 0:
            return "NO"
    return "YES"
    


T = int(input())
while (T):
    # lis = map(int,input().split())
    # num = int(input())
    # solve()
    output = solve()
    print(output)
    T -= 1