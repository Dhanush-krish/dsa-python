### Pointers
    allow you to point to a potentially large segment of memory with just a simple memory address.

##### Advantages
* they don't require sequential storage space.

##### Disadvantages
* need additional space to store the address 

### Node
    A node is a container of data, together with one or more links to other nodes. A link is a pointer.


### Singly linked lists
    1. a list with only one pointer between two successive nodes
    2. can only be traversed in a single direction

##### Advantage
    1. Time complexity is always constant O(1) insertion and deletion of elements at the beginning 
    2. O(1) for insertion and deletion at the  end(only if tail pointer is used) .

##### Disadvantage

    1. Finding an element in linked list would take O(n) because you need to traverse the whole list to find the element



reference
*   https://www.hackerearth.com/practice/data-structures/linked-list/singly-linked-list/tutorial/
*   https://leetcode.com/explore/learn/card/linked-list/
*   https://www.programiz.com/dsa/linked-list
*   https://realpython.com/linked-lists-python/
*   https://leetcode.com/discuss/study-guide/1800120/become-master-in-linked-list