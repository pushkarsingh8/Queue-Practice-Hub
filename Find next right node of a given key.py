#Find next right node of a given key:-

class Node:
    def __init__(self,value):
        self.data = value
        self.right = None
        self.left = None
    
def find_the_key_right_node(root,key):
    if root is None:
        return None
    
    queue = [root]
    
    
    while queue:
        
        size = len(queue) #track number of Nodes in current level
        
    
        
        for i in range(size):
            node = queue.pop(0) #First node is Pop and second is right node will be key
            
            
            
            if node.data  == key: #2 is 2
                return queue[0] if i < size - 1 else None # if node.data have right node or not checking help of size 
            
            if node.left:
                queue.append(node.left)
            

            if node.right:
                queue.append(node.right)
                
                
    return None
            
        
        
    
    
    
    
    
    
root = Node(10)

root.left = Node(2)
root.left.left = Node(8)
root.left.right = Node(4)

root.right = Node(6)
root.right.right = Node(5)

key = 2

result = find_the_key_right_node(root,key)

print(result.data if result else "No right node available")