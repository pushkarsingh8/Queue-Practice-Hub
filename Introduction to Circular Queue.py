#Introduction to Circular Queue:-

class queue:
    def __init__(self,q_size):
        self.arr = [0] * q_size
        self.size = 0
        self.front = 0
        self.rear = -1
        self.capacity = q_size
        
        
        
    def is_empty(self):
        return self.size == 0
    
    
    def isFull(self):
        return self.size == self.capacity
        
        
    def enqueue(self,value):
        if self.isFull():
            print( "queue is full")
            return
        

        self.rear = (self.rear + 1) % self.capacity
        self.arr[self.rear] = value
            
        self.size += 1
        
    
    def dequeue(self):
        if self.is_empty():
            return "empty queue"
        
        self.front = (self.front+1) % self.capacity
        
        self.size -=1
        
        
        
        
    def get_front(self):
        return self.arr[self.front]
    
    
    def get_rear(self):
        return self.arr[self.rear]
    
    
    def traverse(self):
        if self.is_empty():
            return "empty queue"
        
        index = self.front
        res = []
        for _ in range(self.size):
            res.append(self.arr[index])
            index = (index + 1) % self.capacity
        
        return res
    
    
    
q = queue(5)

for i in range(6):
    q.enqueue(i)


res = q.traverse()
print(res)