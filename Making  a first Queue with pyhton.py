#Queue:-

class Node:
    #class making a node of storing a data and store a address of next Node:-
    def __init__(self,value):
        self.data = value
        self.next = None
        
        
class queue:
    
    #Creating a initial value with two variable
    def __init__(self):
        self.front = None
        self.rear = None 
        
    def enqueue(self,value):
        #creating a new node in a Queue
        new_node = Node(value)
        
        if self.rear == None:
            self.front = new_node
            self.rear = self.front
        else:
            self.rear.next = new_node
            self.rear = new_node
            
            
         
    def dequeue(self):
        if self.front == None:
            print("Queue Empty")
        
        else:
            #delete a item in queue
            self.front = self.front.next
            
            
    def is_empty(self):
        #when queue is empty it's return boolean values
        print(self.front == None) 
        
            
    def front_item(self):
        if self.front == None:
            print("Queue is Empty")
            
        else:
            #it's Show Top value of queue
            print(self.front.data)
    
    
    def rear_item(self):
        if self.front == None:
            print("Queue is Empty")
            
        else:
            #it's Show end value of queue
            print(self.rear.data)
    
    
    
    
    def traverse(self):
        if self.front == None:
            print("Queue is Empty")
        
        else:
            temp = self.front
            #it's traverse on the based of address of nodes ->
            while temp!=None:
                print(str(temp.data))
                temp = temp.next
                
                
        
        
        
        
q = queue()
data = [22,45,65,87]
#driver Code to pushing a value in quque
for num in data:
    q.enqueue(num)
    
#Showing all Values in Queue
q.traverse()

print("first Item of Queue",end=":")
q.front_item()

print("End Item of Queue",end=":")
q.rear_item()

#delete a all item in Queue
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
print("Queue is Empty",end=":")
q.is_empty()
q.traverse() #it's return also empty queue
            
