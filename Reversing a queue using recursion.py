#Reversing a Queue Using Recursion:-

class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
        
        
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
        
        
    def is_empty(self):
        return self.front == None
    
        
        
    def enqueue(self,value):
        new_node = Node(value)
        if self.rear == None:
            self.front = new_node
            self.rear = self.front
            self.size += 1
            
        else:
            self.rear.next = new_node
            self.rear = new_node
            self.size += 1
            
            
            
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None
        
        value = self.front.data
        self.front = self.front.next
        self.size -= 1
        
        if self.front == None:
            self.rear = None

        return value   
        

    def recursion_reverse(self):
        if self.is_empty():
            #base case
            return None
        
        value = self.dequeue()
        
        self.recursion_reverse()
        
        self.enqueue(value)
        
        
        
        
    def traverse(self):
        if self.front == None:
            print("Queue is Empty")
            return None
        
        curr = self.front
        res = []
        while curr!=None:
            res.append(curr.data)
            curr = curr.next
            
            
        print("Queue: ",res)

        
        
        
q = Queue()

q.enqueue(3)
q.enqueue(5)
q.enqueue(7)
q.traverse()
q.recursion_reverse()
print("After Reverse: ",end=" ")
q.traverse()

