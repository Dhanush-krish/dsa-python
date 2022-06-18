#   https://www.codechef.com/LP1TO202/problems/BALLOON



import io,os,sys
# import math
# from queue import PriorityQueue
# from collections import defaultdict,deque
# input = sys.stdin.readline
# sys.stdout.write(str(n) + "\n")


def solve():
    num = int(input())
    lis = list(map(int,input().split()))
    count = 0
    
    for index, value in enumerate(lis):
        if value <= 7:
            count += 1
        if count == 7:
            print(index+1)
            break


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
7
1 2 3 4 5 7 6
8
8 7 6 5 4 3 2 1
9
7 4 3 5 6 1 8 2 9
Sample Output 1 
7
8
8
"""