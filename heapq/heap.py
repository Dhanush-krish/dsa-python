import heapq as hq

### Min Heap
minHeap = [5,4,3,2,1]
hq.heapify(minHeap)

## pop smallest elements
print(hq.heappop(minHeap))
print(hq.heappop(minHeap))
print(hq.heappop(minHeap))

# push elements to heap
hq.heappush(minHeap, 10)


maxHeap = []  # empty max heap

# Push numbers (negated for max-heap)
hq.heappush(maxHeap, -10)
hq.heappush(maxHeap, -5)
hq.heappush(maxHeap, -20)

print("Internal heap:", maxHeap)

# Pop max element (remember to negate back)
print("Max element:", -hq.heappop(maxHeap))
print("Next max:", -hq.heappop(maxHeap))








