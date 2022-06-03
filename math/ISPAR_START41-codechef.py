#   https://www.codechef.com/submit-v2/ISPAR

#sample input#
"""
4
4 1
3 3
9 1
3489601027782 8104267
"""

#output#
"""
EVEN
EVEN
ODD
EVEN
"""


def solve():
    l,n = map(int,input().split())
    if (n == 1 and l%2 !=0) or n == 2:
        print("ODD")
    else:
        print("EVEN")
    


T = int(input())
while (T):
    solve()
    T -= 1
    
