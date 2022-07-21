#   https://www.codechef.com/START48D/problems/MAKEPAL2



import io,os,sys
# import math
# from queue import PriorityQueue
# from collections import defaultdict,deque, Counter
# input = sys.stdin.readline
# sys.stdout.write(str(n) + "\n")


def solve():
    num = int(input())
    # lis = map(int,input().split())
    ip_str = list(input())
    right = 0
    left = num-1
    
    while (right > left):
        if ip_str[right] == ip_str[left]:
            left += 1
            right -= 1
        elif (ip_str[left+1]==ip_str[right]):
            ip_str[left] = ""
            left += 1
        else:
            ip_str[right] = ""
            right -= 1
    print("".join(ip_str))
            
            


T = int(input())
while (T):
    # lis = map(int,input().split())
    # num = int(input())
    solve()
    # output = solve()
    # print(output)
    T -= 1