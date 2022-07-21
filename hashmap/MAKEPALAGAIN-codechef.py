#   https://www.codechef.com/LTIME110D/problems/MAKEPALAGAIN




import io,os,sys
# import math
# from queue import PriorityQueue
from collections import defaultdict,deque, Counter
# input = sys.stdin.readline
# sys.stdout.write(str(n) + "\n")


def solve():
    num = int(input())
    # lis = map(int,input().split())
    ip_str = input()
    even  = defaultdict(int)
    odd = defaultdict(int)
    odd = Counter(ip_str[0::2])
    even = Counter(ip_str[1::2])
    
    if odd-even:
        print("NO")
    else:
        print("YES")
        
        
        


T = int(input())
while (T):
    # lis = map(int,input().split())
    # num = int(input())
    solve()
    # output = solve()
    # print(output)
    T -= 1