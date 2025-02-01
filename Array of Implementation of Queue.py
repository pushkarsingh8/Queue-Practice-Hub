#Array of Implement in Queue with the behaviour of Queues:-


class queue:
    def __init__(self,q_size):
        self.arr = [0]*q_size 
        self.size = 0
        self.capacity = q_size
        self.front = 0
        self.rear = -1
        
        
        
    def enqueue(self,value):
        
        if self.size == self.capacity:
            return 
        
        else:
            self.rear = (self.rear + 1) % self.capacity
            
            self.arr[self.rear] = value
            self.size += 1    
            
    
    def dequeue(self):
        if self.size == 0:
            return 
        
        #shifting all elements right to left
        else:
            self.front = (self.front + 1) % self.capacity
            self.size -= 1
            
            
    def get_front(self):
        if self.size == 0:
            return -1
        else:
            
            return self.arr[self.front]
                
                
    def traverse(self):
        res = []
        for num in range(self.size):
            index = (self.front + num) % self.capacity
            res.append(self.arr[index])
        
        print(res)
    
    
    
q = queue(5)
for num in range(1,6):
    
    q.enqueue(num)
    
q.dequeue()
q.dequeue()
q.traverse()
print(q.get_front())

        
        
                    
        