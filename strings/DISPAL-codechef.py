#   https://www.codechef.com/submit-v2/DISPAL?tab=statement



def solve():
    n,x = map(int,input().split())
    min_num = (2*x)-1

    if(n>=min_num):
        temp = ["z" for _ in range(n)]
        for index in range(x):
            temp[index] = chr(97+index)
            temp[n-1-index] =  chr(97+index)
        print("".join(temp))

    else:
        print(-1)
    


T = int(input())
while (T):
    solve()
    T -= 1