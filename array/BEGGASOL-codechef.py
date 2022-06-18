#   https://www.codechef.com/LP1TO202/problems/BEGGASOL


import io,os,sys
# import math
# from queue import PriorityQueue
# from collections import defaultdict,deque
# input = sys.stdin.readline
# sys.stdout.write(str(n) + "\n")


def solve():
    num = int(input())
    lis = list(map(int,input().split()))
    meter = lis[0]
    covered_distance = lis[0]
    
    for index in range(1,num):
        meter -= 1
        covered_distance += lis[index]
        meter += lis[index]
        if meter == 0:
            break
    
    print(covered_distance)
        
    


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
3
5
3 0 0 0 0
5
1 1 1 1 1
5
5 4 3 2 1
Sample Output 1 
3
5
15
"""