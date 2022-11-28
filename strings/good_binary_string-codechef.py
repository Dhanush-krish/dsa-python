def solve():
    # LEN = int(input())
    # lis = map(int,input().split())
    string = "10100"
    zi = set()
    iz = set()
    
    for index in range(1, len(string)-1):
        if string[index-1:index+1] == '10':
            iz.add(index-1)
        if string[index-1:index+1] == '01':
            zi.add(index-1)
        if string[index:index+2] == '10':
            iz.add(index)
        if string[index:index+2] == '01':
            zi.add(index)

    t_iz, t_zi = len(iz), len(zi)
    
    
    # for index in range()
    print(zi)
    print(iz)


    

solve()
# T = int(input())
# while (T):
#     # lis = map(int,input().split())
#     # num = int(input())
#     solve()
#     # output = solve()
#     # print(output)
#     T -= 1