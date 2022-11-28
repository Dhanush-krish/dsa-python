from collections import deque

queue = deque([3,7,6,4])
ans = 0
while(len(queue)> 1):
    first = queue[0]
    last = queue[-1]
    if first == last:
        queue.pop()
        queue.popleft()
    elif first  > last:
        queue[0] = first - last
        queue.pop()
        ans += 1
    else:
        queue[-1] = last - first
        queue.popleft()
        ans += 1
print(ans)
