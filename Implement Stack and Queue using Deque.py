#Implement Stack and Queue using Deque:-

class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
        
        
class deque:
    #double ended queue
    def __init__(self):
        
        self.head = None
        self.tail = None
        self.size = 0
        
        
    def is_empty(self):
        return self.head == None
        
        
    def len(self):
        return self.size
        
        
    def insert_head(self,value):
        new_node = Node(value)
        
        if self.is_empty():
            self.head = new_node
            self.size += 1
            
        else:
            #inserting from head on Top value
            new_node.next = self.head
            self.head = new_node
            self.size += 1
            
            
    
    def insert_tail(self,value):
        new_node = Node(value)
        
        if self.is_empty():
            self.head = new_node
            self.tail = self.head
            
            
        else:
            
            self.tail.next = new_node
            self.tail = new_node
        
        self.size += 1
    

    def delete_head(self):
        if self.head == None:
            print("Empty")
            return None
        
        self.head = self.head.next
        self.size -= 1
             
        
    def delete_tail(self):
        if self.is_empty():
            print("Empty")
            return None
        
        if self.head == None:
            self.tail = None
            self.size -= 1
            return
        
        
        curr = self.head
        while curr.next.next != None:
            curr = curr.next
            
        curr.next = None
        self.tail = curr
        self.size -= 1
        
        
    def display(self):
        if self.is_empty():
            print("Empty")
            return None
        curr = self.head
        res = []
        while curr!=None:
            res.append(curr.data)
            curr = curr.next
        return res

    
        
        
        
class stack:
    def __init__(self):
        self.stack = deque()
        
    def len(self):
        return self.stack.len()
        
    def is_empty(self):
        return self.stack.is_empty()
        
    def push(self,value):
        self.stack.insert_head(value)
        
    def pop(self):
        self.stack.delete_head()
        
    
    def display(self):
        return self.stack.display()        

        
        
        
        
class Queue:
    def __init__(self):
        
        self.queue = deque()
        
    def len(self):
        return self.queue.len()
    
        
    def is_empty(self):
        return self.queue.is_empty()
            
        
    def enqueue(self,value):
        self.queue.insert_tail(value)
        
    def dequeue(self):
        self.queue.delete_head()
        
    def display(self):
        return self.queue.display()        


        
        
    
s = stack()
q = Queue()

s.push(5)
q.enqueue(5)

s.push(4)
q.enqueue(4)
s.push(1)
q.enqueue(1)
q.enqueue(99)

q.dequeue()

result = s.display()
print("Stack Output: ",result,"using [LIFO]")

result = q.display()
print("Queue Output: ",result,"using [FIFO]")