#Queue:-

class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
        
        
class queue:
    
    
    def __init__(self):
        self.front = None
        self.rear = None 
        
    def enque(self,value):
        new_node = Node(value)
        if self.rear == None:
            self.front = new_node
            self.rear = self.front
        else:
            self.rear.next = new_node
            self.rear = new_node
            
            
         
    def dequeue(self):
        if self.front == None:
            print("Queue Empty")
        
        else:
            self.front = self.front.next
            
    def traverse(self):
        if self.rear == None:
            print("Queue is Empty")
        
        else:
            temp = self.front
            
            
            while temp!=None:
                print(str(temp.data))
                temp = temp.next
        
        
        
q = queue()
q.enque(4)
q.enque(5)
q.enque(7)
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.traverse()
            
