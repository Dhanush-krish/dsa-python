'''

    Data contains the value to be stored in the node.
    Next contains a reference to the next node on the list.

'''

from dataclasses import dataclass


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
    

class LinkedList:
    def __init__(self, data = []):
        
        if data != []:
            self.tail = Node(data.pop(0))
            self.head = self.tail
            
            for element in data:
                self.tail.next = Node(element)
                self.tail = self.tail.next
                
                
    def traverse(self):
        
        node = self.head
        while (node is not None):
            print(node.data, "->",end = " ")
            node = node.next
        print(None)
        
    def append(self, element):
        
        if self.head is not None:
            self.tail.next = Node(element)
        else:
            self.head = Node(element)


    def prepend(self, element):
        
        if self.head is None:
            self.head = Node(element)
        else:
            new_head = Node(element)
            new_head.next = self.head
            self.head = new_head
            
    def insert(self, position, element):

        new_node = Node(element)
        if self.head is None:
            self.head = new_node
            
        else:
            if position == 0:
                new_node.next = self.head
                self.head = new_node
            else:
                position -= 1
                self.ins_pos = self.head
                
                while (self.ins_pos.next is not None and position>0):
                    self.ins_pos = self.ins_pos.next
                    position -= 1
                    
                print(self.ins_pos.data)
                    
                new_node.next = self.ins_pos.next
                self.ins_pos.next = new_node
        



obj = LinkedList([4,1,4,5,6])
obj.traverse()
obj.append(10)
obj.traverse()
obj.prepend(8)
obj.traverse()
obj.insert(0, 20)
obj.traverse()


