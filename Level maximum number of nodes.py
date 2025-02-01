#Level Maximum number of Nodes:-

class Node:
    def __init__(self,value):
        self.data = value
        self.left = None
        self.right = None
    
    
def find_level_max_nodes(root):
    
    if root == None:
        return 

    queue = [root]
    max_nodes = 0
    
    max_level = -1
    
    curr_level = 0 
    
    while queue:
        
        level_size = len(queue)
        
        if level_size>max_nodes:
            max_nodes = level_size
            max_level = curr_level
            
            
        
        for _ in range(level_size):
            curr_node = queue.pop(0)
            
            if curr_node.left:

                queue.append(curr_node.left)

            if curr_node.right:

                queue.append(curr_node.right)
                
        curr_level+=1
                
                
    return max_level
    
    
    
    
    
root = Node(2)
root.left = Node(1)

root.right = Node(3)

root.left.left = Node(4)

root.left.right = Node(6)

root.left.right.left = Node(5)

root.right.right = Node(8)
        
print("Level: ",find_level_max_nodes(root))