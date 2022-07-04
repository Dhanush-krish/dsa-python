#   https://leetcode.com/explore/learn/card/linked-list/209/singly-linked-list/1290/

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        
        if index < 0 or index >= self.size:
            return -1
        
        if self.head is None:
            return -1
        node = self.head
        
        for _ in range(index):
            node = node.next
        return node.data

    def addAtHead(self, val: int) -> None:
        

        new = Node(val)
        new.next = self.head
        self.head = new
        self.size += 1

    def addAtTail(self, val: int) -> None:
        
        if self.head is None:
            self.head = Node(val)
        else:
            node = self.head
            while(node.next is not None):
                node = node.next
            node.next = Node(val)
        self.size += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return 
        if index == 0:
            self.addAtHead(val)
        else: 
            node = self.head
            new = Node(val)
            for _ in range(index - 1):
                node = node.next
            new.next = node.next
            node.next = new
            
        self.size += 1
                
        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return 
        node = self.head
        if index == 0:
            self.head = node.next 
        else:
            for _ in range(index-1):
                node = node.next
            node.next = node.next.next
        self.size -= 1
            
        
class Node():
    def __init__(self,value):
        self.data = value
        self.next = None

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(0) 
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)