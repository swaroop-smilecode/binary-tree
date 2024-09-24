from binary_tree import root_node

def depth_first_values(root_node):
    if not root_node:
     return []
    
    stack = [root_node]
    result = []

    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.right:
            stack.append(node.right)   
        if node.left:
            stack.append(node.left)

    return result

result = depth_first_values(root_node)
print(result)

  
   
