#### Priority Queue
* a priority queue is an abstract data type similar to a regular queue or stack
* additionally has a "priority" associated with it
* an element with high priority is served before an element with low priority


**A priority queue is an abstract data type, while a Heap is a data structure. Therefore, a Heap is not a Priority Queue, but a way to implement a Priority Queue**

#### Definition of Heap
According to Wikipedia, a Heap is a special type of binary tree. A heap is a binary tree that meets the following criteria:

* Is a complete binary tree;
* The value of each node must be no greater than (or no less than) the value of its child nodes.

##### A Heap has the following properties:

* Insertion of an element into the Heap has a time complexity of  O(logN);
* Deletion of an element from the Heap has a time complexity of  O(logN);
* The maximum/minimum value in the Heap can be obtained with O(1) time complexity.


##### Classification of Heap
There are two kinds of heaps: Max Heap and Min Heap.

**Max Heap**: Each node in the Heap has a value no less than its child nodes. Therefore, the top element (root node) has the largest value in the Heap.

**Min Heap**: Each node in the Heap has a value no larger than its child nodes. Therefore, the top element (root node) has the smallest value in the Heap.

##### Application of Heap
1. Heap Sort
2. The Top-K problem
3. The K-th element
