from binary_tree import root_node

def depth_first_values(root_node):
    if not root_node:
     return []
    
    right_values = depth_first_values(root_node.right)
    left_values = depth_first_values(root_node.left)
    return [root_node.val, *left_values, *right_values]

result = depth_first_values(root_node)
print(result)