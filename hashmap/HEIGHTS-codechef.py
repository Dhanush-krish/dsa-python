#   https://www.codechef.com/START47D/problems/HEIGHTS



import io,os,sys
# import math
# from queue import PriorityQueue
from collections import defaultdict,deque, Counter
# input = sys.stdin.readline
# sys.stdout.write(str(n) + "\n")


def solve():
    n = int(input())
    lis = list(map(int,input().split()))
    single = 0
    min_count = -sys.maxsize
    max_key = 0
    freq = dict(Counter(lis))
    
    for key,values in freq.items():
        if values == 1:
            single += 1
        else:
            min_count = max(min_count, values)
        max_key = max(max_key, key)
        
    if single == 1 and freq[max_key] == 1:
        if min_count > 2 :
            return 1
        else:
            return 2
    else:
        return ((single+1)//2) 

T = int(input())
while (T):
    # lis = map(int,input().split())
    # num = int(input())
    # solve()
    output = solve()
    print(output)
    T -= 1