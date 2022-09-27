for _ in range(int(input())):
    hmap = {}
    for _ in range(int(input())):
        
        low, high = map(int, input().split())
        #update the hashmap
        for key in range(low, high+1):
            hmap[key] = hmap.get(key,0) + 1
        
        #find max people  and its largest interval
        people = list(hmap.values())
        maxi = max(people)
        result, count = 0, 0
        for value in people:
            if value == maxi:
                count += 1
                result = max(result, count)
            else:
                count = 0
                
        print("ans =",result)        
    