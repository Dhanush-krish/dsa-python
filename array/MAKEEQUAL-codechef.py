#   https://www.codechef.com/LP1TO202/problems/MAKEEQUAL


import io,os,sys
# import math
# from queue import PriorityQueue
# from collections import defaultdict,deque
# input = sys.stdin.readline
# sys.stdout.write(str(n) + "\n")


def solve():
    num = int(input())
    lis = list(map(int,input().split()))
    print(max(lis) - min(lis))


T = int(input())
while (T):
    # lis = map(int,input().split())
    # num = int(input())
    solve()
    # output = solve()
    # print(output)
    T -= 1


"""
Sample Input 1 
2
3
1 3 1
3
2 2 2
Sample Output 1 
2
0
"""