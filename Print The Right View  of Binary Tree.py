#Print Right View of Binary Tree:-

class Node:
    def __init__(self,value):
        self.data = value
        self.right = None
        self.left = None
        
        

def print_right_view():
    
    if root == None:
        print("Empty")
        return None
    
    queue = [root]
    
    while queue:
        
        level_size = len(queue)
        
        
        for i in range(level_size):
            
            node = queue.pop(0)
            
            if i == level_size - 1:
                print(node.data,end=" ")
                
                
                
            if node.left:
                queue.append(node.left)
        
            if node.right:
                queue.append(node.right)
        
        
    
    
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.left = Node(4)
root.right.right = Node(5)


print_right_view(root)
