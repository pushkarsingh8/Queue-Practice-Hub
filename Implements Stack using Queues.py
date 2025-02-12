#Impelement stack using queues:-

class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
        
        
class queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
        
    def is_empty(self):
        return self.front == None    
        
    
    def enqueue(self,value):
        new_node = Node(value)

        if self.is_empty():
            self.front = self.rear = new_node
            
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size += 1
        
        
        
        
    def dequeue(self):
        if self.is_empty():
            print("Empty")
            return None
        data = self.front.data
          
        self.front = self.front.next
        
        if self.front == None:
            self.rear = None
            
        self.size -= 1
        return data
        
        
class stackusingqueues:
    def __init__(self):
        self.q1 = queue()
        self.q2 = queue()
        
        
    def is_empty(self):
        return self.q1.is_empty()
        
        
    def push(self,value):
        self.q2.enqueue(value)
        
        while not self.q1.is_empty():
            self.q2.enqueue(self.q1.dequeue())
            
            
            
        self.q1,self.q2 = self.q2,self.q1
            
            
        
        
        
    def pop(self):
        
        if self.is_empty():
            return None
        return self.q1.dequeue()
        
        
    def traverse(self):
        
        
        if self.is_empty():
            print("stack is empty")
            return None
        
        
        curr = self.q1.front
        res = []
        while curr!=None:
            res.append(curr.data)
            curr = curr.next 
            
        print(res)
        

q = stackusingqueues()
q.push(10)
q.push(9)
q.push(80)
q.pop()
q.traverse()