#   https://www.codechef.com/submit/MINLCS

#   T(N) => O(n)
#   S(N) => O(n)
# where n is the length of string



import io,os,sys
# import math
# from queue import PriorityQueue
from collections import defaultdict,deque, Counter
# input = sys.stdin.readline
# sys.stdout.write(str(n) + "\n")


def solve():
    LEN = int(input())
    # lis = map(int,input().split())
    str1 = "abcde"
    str2 = "cdefg"
    freq1 = Counter(str1)
    freq2 = Counter(str2)

    result = 0
    for key,value in freq1.items():
        if key in freq2:
            result = max(result, min(value, freq2[key]))

    print(result)

        
    


T = int(input())
while (T):
    # lis = map(int,input().split())
    # num = int(input())
    solve()
    # output = solve()
    # print(output)
    T -= 1