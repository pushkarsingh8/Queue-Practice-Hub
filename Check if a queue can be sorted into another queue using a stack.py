#Check if a queue can be sorted into another queue using a stack:-
class Node:
    
    def __init__(self,value):
        self.data = value
        self.next = None

class queue:
        
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0
        
        
    def len(self):
        print(self.size)
        
    
    def push(self,value):
        new_node = Node(value)
        if self.rear == None:
            self.front = new_node
            self.rear = self.front
            self.size += 1
            
        else:
            self.rear.next = new_node
            self.rear = new_node
            self.size += 1
            
    def pop(self):
        if self.front == None:
            return None
        if self.front == None:
            self.rear = None
        
        else:
            data = self.front.data
            self.size -= 1
            self.front = self.front.next
            
            return data
        
        
    def check_sorted(self):
        if self.front == None:
            return True
        
        st = []
        
        curr = self.front
        expected = 1
        
        while curr!=None:
            
            if curr.data == expected:
                expected +=1
                

            else:
                if st and st[-1] < curr.data:
                    
                    
                    return False
                
            st.append(curr.data)
                
            curr = curr.next
            
            
        while st:


            if st.pop() != expected:
                return False
            
            expected+=1
            
        return True
                    
            
        
        
        
        
        
        
        
    def traverse(self):
        if self.front == None:
            print("Empty Queue")
            
        res = []
        curr = self.front
        
        while curr!=None:
            res.append(curr.data)
            curr = curr.next
            
        if res:
            
            print("Output:",res)
            
        
        
        
        
        
    
        
            
            
    
    
    
    
    
    
    
q = queue()
q.push(6)
q.push(5)
q.push(4)
q.push(3)
q.push(2)
q.push(1)
res = q.check_sorted()
q.traverse()
print(res)

