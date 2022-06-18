#   https://www.codechef.com/LP1TO202/problems/SUBTASK



import io,os,sys
# import math
# from queue import PriorityQueue
# from collections import defaultdict,deque
# input = sys.stdin.readline
# sys.stdout.write(str(n) + "\n")


def solve():
    # num = int(input())
    n, m, k = map(int,input().split())
    result = list(map(int, input().split()))

    if sum(result) == n:
        print(100)
    elif sum(result[:m]) == m:
        print(k)
    else:
        print(0)
        
    

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
4
4 2 50
1 0 1 1
3 2 50
1 1 0
4 2 50
1 1 1 1
5 3 30
1 1 0 1 1
Sample Output 1 
0
50
100
0
"""