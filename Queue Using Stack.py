#Queue using a Stack:-

class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
        
        
class stack:
    #fully stack 
    
    def __init__(self):
        self.top = None
        self.size = 0
        
    def is_empty(self):
        
        return self.top == None
        
        
    def push(self,value):
        new_node = Node(value)
        #if stack is empty
        
        if self.is_empty():
            self.top = new_node
            self.size += 1
            
        else:
            #if have elements
            new_node.next = self.top
            self.top = new_node
            self.size += 1
            
            
    def pop(self):
        if self.is_empty():
            print("Queue is Empty")
            return None
             
        data = self.top.data
        self.top = self.top.next
        self.size -= 1
        return data
    
    
class Queue:
    
    def __init__(self):
        #it's inherit the behaviour of Stack class
        self.st1 = stack()
        self.st2 = stack()
        
        
        
    def enqueue(self,value):
        #it's queue style to insert a elements
        while not self.st1.is_empty():
            self.st2.push(self.st1.pop())
            
        self.st1.push(value)
            
        
        
        while not self.st2.is_empty():
            
            self.st1.push(self.st2.pop())
        
        
        
        
    def dequeue(self):
        if self.st1.is_empty():
            print("Queue is Empty")
            return None
        return self.st1.pop()
        
        
    def traverse(self):
        res = []
        curr = self.st1.top

        while curr!=None:
            res.append(curr.data)
            curr = curr.next
            
        print("Queue:",res)
        
        
        
        
    
    
    
    
    
q = Queue()
q.enqueue(5)
q.enqueue(7)
q.enqueue(3)
q.dequeue()
q.enqueue(9)

q.traverse()
