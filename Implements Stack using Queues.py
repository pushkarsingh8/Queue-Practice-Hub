#Implement Using Queues:-

class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
        
class stack:
            
    def __init__(self):
        self.top = None
        self.size = 0
        
    def is_empty(self):
        return self.top == None
    
    def push(self,value):
        new_node = Node(value)
        
        new_node.next = self.top
        self.top = new_node
        self.size += 1
        
        
    def pop(self):
        if self.is_empty():
            return None
        
        value = self.top.data
        self.top = self.top.next
        self.size -= 1
        return value
        
        
        
        
        
        
class two_stack:
    def __init__(self):
        self.q1 = stack()
        self.q2 = stack()
        
        
        
    def push(self,value):
        
        self.q2.push(value)
        
        
        
        
        
        #transfer all the elements q1 to q2
        while not self.q1.is_empty():
        
            
            
            self.q2.push(self.q1.pop())
            
        #swap q1 to q2  
        self.q1, self.q2 =self.q2, self.q1
        
        
    def pop(self):
        
        if self.q1.is_empty():
            print("stack is Empty")
            return None
        
        return self.q1.pop()
    
        
        
    
        
                
        
        
    def traverse(self):
        if self.q1.is_empty():
            print("Stack is Empty")
            return None
        
        curr = self.q1.top
        res = []
        
        while curr!=None:
            res.append(curr.data)
            curr =  curr.next
        
        print(res)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
                
s = two_stack()

s.push(5)
s.push(8)
s.pop()
s.push(8)
s.push(8)
s.traverse()


            
             
        
        
            
