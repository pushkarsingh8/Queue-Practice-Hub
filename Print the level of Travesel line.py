#Print The Level Order of Travesal Line by Line:-

class Node:
    def __init__(self,value):
        self.data = value
        self.left = None
        self.right = None
        
def print_the_level_order_line_by_line(root):
    if root == None :
        return 
    queue = []
    queue.append(root)
    
    while queue:
        
        level_size = len(queue)
        level_nodes = []
            
            
        for _ in range(level_size):
            curr_node = queue.pop(0) #it's behaviour like dequeue FIFO
            level_nodes.append(curr_node.data)
            
            if  curr_node.left:
                queue.append(curr_node.left)
                
            if curr_node.right:
                queue.append(curr_node.right)
                
                
                
        print(" ".join(map(str,level_nodes)))
        
    
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.right.right = Node(5)
root.right.left = Node(4)

root.left.right = Node(7)
root.left.left = Node(6)
        
print_the_level_order_line_by_line(root)
        
            
        
        
        
        
        