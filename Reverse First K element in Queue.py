#Reverse First K element in Queue:-

class Node:
    def __init__(self,value):
        self.data = value
        self.next = None
        
class Queue:
    def __init__(self):
        self.front = None #which using for deleting a node name of "dequeue"
        self.rear = None  #which using for inserting a node name of "enqueue" 
        self.count = 0  #keep tracking a node elements in queue
        
    def __len__(self):
        return self.count
        
 
    def enqueue(self,value):
        new_node = Node(value)
        if self.rear == None:
            self.front = new_node
            self.rear = self.front
            
            
            
        else:
            self.rear.next = new_node
            self.rear = new_node
        
        self.count += 1
        
        
        
    def dequeue(self):
        if self.front == None:
            self.rear = None
            return  None
        
        
        else:
            data = self.front.data
            self.front = self.front.next
            self.count-=1
            return data
            
            
    def traverse(self):
        res = []
        if self.rear == None:
            print('queue empty')
        else:
            res = []
            temp = self.front
            
            while temp!=None:
                res.append(temp.data) 
                temp = temp.next
                
        print(res)
                
                
    def reverse_First_K(self,k):
        if k <= 0 or k > self.count:
            print("Invalid Value of k")
            return 
        
        stack = []
        
        #inserting a element of k items & removing a k elements
        
        for _ in range(k):
            stack.append(self.dequeue())
            
        
        
        while stack:
            #inserting a element in a reverse order at the end of existing elements
            self.enqueue(stack.pop())
            
        for _ in range(self.count - k):
            self.enqueue(self.dequeue())
            
            
            
            
            
        
            
            
            
            
            
queue =  Queue()

for num in range(1,6):
    queue.enqueue(num)
    
queue.reverse_First_K(3)

queue.traverse()            