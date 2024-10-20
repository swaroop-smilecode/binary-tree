from binary_tree import root_node
from collections import deque

def breadth_first_values(root_node):
    if not root_node:
     return []
    
    queue = deque([root_node])
    result = []

    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)   
        if node.right:
            queue.append(node.right)

    return result

result = breadth_first_values(root_node)
print(result)