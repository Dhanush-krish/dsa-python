#   https://www.codechef.com/LP1TO202/problems/VACCINQ

import io, os, sys

# import math
# from queue import PriorityQueue
# from collections import defaultdict,deque
# input = sys.stdin.readline
# sys.stdout.write(str(n) + "\n")


def solve():
    # num = int(input())
    n, p, x, y = map(int, input().split())
    queue = list(map(int, input().split()))
    time_taken = 0
    for index in range(p):
        if queue[index] == 1:
            time_taken += y
        else:
            time_taken += x

    print(time_taken)


T = int(input())
while T:
    # lis = map(int,input().split())
    # num = int(input())
    solve()
    # output = solve()
    # print(output)
    T -= 1

"""
#   sample input
3
4 2 3 2
0 1 0 1
3 1 2 3
1 0 1
3 3 2 2
1 1 1

# sample output
5
3
6
"""
