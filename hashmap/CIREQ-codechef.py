#   https://www.codechef.com/START48D/problems/CIREQ


import io,os,sys
# import math
# from queue import PriorityQueue
from collections import defaultdict,deque, Counter
# input = sys.stdin.readline
# sys.stdout.write(str(n) + "\n")


def solve():
    num = int(input())
    lis = list(map(int,input().split()))
    freq = sorted(Counter(lis).items(), key = lambda item: item[0])
    result = freq[0][1]
    minus = freq[0][1]
    
    for index in range(1,len(freq)):
        if freq[index][1] - minus > 0:
            result += freq[index][1] - minus
            minus += freq[index][1] - minus
    return result


T = int(input())
while (T):
    # lis = map(int,input().split())
    # num = int(input())
    solve()
    # output = solve()
    # print(output)
    T -= 1