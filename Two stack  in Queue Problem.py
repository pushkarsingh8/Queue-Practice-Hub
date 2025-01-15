#Queue Make With help of Two Stack:-
class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
        
class stack:

    def __init__(self):
        self.top = None
        
        
    def is_empty(self):
        return self.top == None
    
    
    def pop(self):
        if self.top == None:
            return None
        else:
            data = self.top.data
            self.top = self.top.next
            return data
        
        

    def push(self,value):
        new_node = Node(value)
        
        if self.is_empty():
            self.top = new_node
            
        else:
            new_node.next = self.top
            self.top = new_node
            
class twostack:
    #intialize value new two stacks
    def __init__(self):
        self.s1 = stack()
        self.s2 = stack()
        
        
    def enqueue(self,value):
        self.s1.push(value)
        
        
    def dequeue(self):
        if self.s2.is_empty():
            
            while not self.s1.is_empty():
                self.s2.push(self.s1.pop())
                
        return self.s2.pop()  
                
            
            
            
    def traverse(self):
        temp_s2= self.s2.top
        #dequeue traverse
        
        while temp_s2!=None:
            print(temp_s2.data,end=" ")
            temp_s2 = temp_s2.next
            
        #enequeue traverse 
        temp_s1 = self.s1.top
        stack_contents = []
        while temp_s1:
            
            stack_contents.append(temp_s1.data)
            temp_s1 = temp_s1.next
            
        #reverse orignal data  
        for data in reversed(stack_contents):
            print(data,end=" ")
            
        print()
            

queue = twostack()            
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)

queue.traverse()

queue.dequeue() 

queue.traverse()
# queue.dequeue() 
# queue.traverse()          
            