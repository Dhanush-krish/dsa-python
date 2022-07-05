#   https://www.codechef.com/COOK143D/problems/KMEX


import io,os,sys
# import math
# from queue import PriorityQueue
# from collections import defaultdict,deque
# input = sys.stdin.readline
# sys.stdout.write(str(n) + "\n")


def solve():
    # num = int(input())
    n,m,k = map(int,input().split())
    lis = list(map(int, input().split()))
    lis.sort()
    mex = 0
    for index in range(m):
        if mex == lis[index]:
            mex += 1
    if mex >= k and n-lis.count(k)>=m:
        print("YES")
    else:
        print("NO")


T = int(input())
while (T):
    # lis = map(int,input().split())
    # num = int(input())
    solve()
    # output = solve()
    # print(output)
    T -= 1