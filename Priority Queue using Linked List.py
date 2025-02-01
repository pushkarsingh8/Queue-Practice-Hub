#Priority Queue using Linked List:-
class Node:
    
    def __init__(self,value,pry):
        self.data = value
        self.pry = pry #priority [Descending order] On a Based of [Value]
        self.next = None
        
class linked_list:
    def __init__(self):
        self.head = None
        
        
    def push(self,value,pry):
        new_node = Node(value,pry)
        
        if self.head == None:
            self.head = new_node
            return
        
        
        if new_node.pry > self.head.pry:
            new_node.next = self.head
            self.head = new_node
            return
                
        
        temp = self.head
        while temp.next != None and temp.next.pry > new_node.pry:
            temp = temp.next
                    
                
                
        new_node.next = temp.next
        temp.next = new_node
                
        
    def pop(self):
        if self.head == None:
            print("Empty")
            return None 
        
        self.head = self.head.next

    def peek(self):
        if self.head == None:
            return None
        return self.head.data
    
    
    
    
    def traverse(self):
        if self.head == None:
            print("Empty")
            return None
        temp = self.head
        res = []
        while temp!=None:
            res.append(temp.data)
            temp = temp.next
            
        print("Output: ",res)
    

l = linked_list()

l.push(4, 1)
l.push(5, 2)
l.push(6, 3)
l.push(7, 0)

l.push(8,99)
        
        
l.traverse()