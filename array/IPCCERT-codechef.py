#   https://www.codechef.com/LP1TO202/problems/IPCCERT

import io,os,sys
# import math
# from queue import PriorityQueue
# from collections import defaultdict,deque
# input = sys.stdin.readline
# sys.stdout.write(str(n) + "\n")


def solve():
    # num = int(input())
    n, m, k = map(int,input().split())
    eligible = 0
    
    for _ in range(n):
        lecture = list(map(int, input().split()))
        questions = lecture.pop()
        if (sum(lecture) >= m) and (questions <= 10):
            eligible += 1
    
    print(eligible)
    

solve()
    
    
"""
Sample Input 1 
4 8 4
1 2 1 2 5
3 5 1 3 4
1 2 4 5 11
1 1 1 3 12
Sample Output 1 
1
"""