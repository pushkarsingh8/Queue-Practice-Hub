#Queue Have Two Operation Get-min Get-max:

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
    
    
    def __len__(self):
        return self.size
        
        
        
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
        if self.front == None:
            self.rear = None
            return
        
        else:
            value = self.front.data
            self.front = self.front.next
            self.size -= 1
            return value   
        
        
    def get_min(self):
        curr = self.front
        min_v = self.front.data
        
        while curr!=None:
            min_v = min(curr.data,min_v)
            
            curr = curr.next
            
        return min_v
        
        
        
        
    def get_max(self):
        max_v = self.front.data
        curr = self.front
        
        
        while curr!=None:    
            
            max_v = max(curr.data,max_v)
            
            curr = curr.next
            
        
        return max_v
        
        
        
        
        
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


q.enqueue(5)
q.enqueue(7.6)
q.enqueue(7)
q.enqueue(2)


q.traverse()

print(f"Max: {q.get_max()}\nMin: {q.get_min()}")