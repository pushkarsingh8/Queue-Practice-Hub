#Implementation of Deque using circular array:-

class queue:
    def __init__(self,q_size):
        self.arr = [0] * q_size
        self.size = 0
        self.front = -1
        self.rear = -1
        self.capacity = q_size
        
        
        
    def is_full(self):
        return self.size == self.capacity
    
    def is_empty(self):
        return self.size == 0
    
    
    def get_rear(self):
        return (self.arr[self.rear])
    
    
    def get_front(self):
        return (self.arr[self.front])
    
    
    def insert_front(self,value):
        if self.is_full():
            print("Queue is Full")
            return
            
        else:
            if self.front == -1:
                self.front = 0
                self.rear = 0
                
                
            else:
                self.front = (self.front - 1 + self.capacity) % self.capacity
                
                
            self.arr[self.front] = value
            
            self.size += 1
            
    
    def insert_rear(self,value):
        if self.is_full():
            print("Queue is Full")
            return
            
        else:
            if self.rear == -1:
                self.front = 0
                self.rear = 0
                
                
            else:
                self.rear = (self.rear + 1 ) % self.capacity
                
                
            self.arr[self.rear] = value
            
            self.size += 1
            
            
            
    def delete_front(self):
        
        if self.is_empty():
            print("Queue is Empty")
            return
        
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
            
            
        else:
            self.front = (self.front + 1) % self.capacity
        self.size -= 1
            
    
    def delete_rare(self):
        
        if self.is_empty():
            print("Queue is Empty")
            return
        
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
            
            
        else:
            self.rear = (self.rear + 1) % self.capacity
        self.size -= 1
             
                     
    
    
    
    
       
        
    def traverse(self):
        if self.front == None:
            return "queue is empty"
        
       
        res = []
        index = self.front
            
        for _ in range(self.size):
            
            res.append(self.arr[index])
            index = (index +  1) % self.capacity
            
        return res 
            
        
q = queue(10)
q.insert_rear(5)
q.insert_rear(4)
q.insert_rear(3)
q.insert_rear(2)


res = q.traverse()

print("Result:",res)

get_front = q.get_front()

print("First Element of Queue:",get_front)

get_rare = q.get_rear()

print("Last Element of Queue:",get_rare)

