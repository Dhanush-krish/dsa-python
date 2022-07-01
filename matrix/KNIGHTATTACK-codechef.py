#   https://www.codechef.com/START44D/problems/KNIGHTATTACK


import io,os,sys
# import math
# from queue import PriorityQueue
# from collections import defaultdict,deque
# input = sys.stdin.readline
# sys.stdout.write(str(n) + "\n")
def attack_pos(x, y):
    pos =  [(x-1,y-2),(x-2,y-1),(x-2,y+1),(x-1,y+2),
            (x+1,y-2),(x+2,y-1),(x+2,y+1),(x+1,y+2)]
    
    final = [(x, y) for x,y in pos if x>=1 and x <=8 and y <= 8 and y >= 1]
    return final

def solve():
    # num = int(input())
    x1,y1 = map(int,input().split())
    x2,y2 = map(int,input().split())
    
    pos1 = attack_pos(x1, y1)
    pos2 = attack_pos(x2, y2)
    
    for loc1 in pos1:
        for loc2 in pos2:
            if loc1 == loc2:
                return("YES")
    return("NO")


T = int(input())
while (T):
    # lis = map(int,input().split())
    # num = int(input())
    output = solve()
    print(output)
    T -= 1
    
"""
Sample Input 1 
4
1 1
1 2
1 1
1 3
1 1
1 4
1 1
1 5
Sample Output 1 
NO
YES
NO
YES
"""