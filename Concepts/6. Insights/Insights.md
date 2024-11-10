#### Why DFS & BFS are bahaving the way they are behaving?
Basically a tree can be traversed by using one of the following algorithms.
1. DFS</br>
2. BFS</br>

When we traverse a tree using DFS, we explore the tree in Depth first pattern,</br> 
where as when we traverse using the BFS, we explore the tree in Breadth frist pattern.</br> 
Because of what reason, the algorithms behaving in such a way?</br>

The answer lies in the data structure we use in these Algorithms.</br>
In DFS, we use stack & in BFS, we use Queue.</br> 
This is the primary reason why DFS explores the tree in Depth First</br>
where as BFS explores the tree in Breadth first.
This can be better understood with the help of code</br>

<ins>DFS:</ins>
```python
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
```
<ins>BFS:</ins>
```python
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
```
#### When to use DFS & when to use BFS?
If the problem is asking for `closest path` / `smallest path`, then go for `BFS`, else `DFS`.

#### Max path sum problem has special edge case
```python
def max_path_sum(root):
    if root is None:
        return float("-inf")
    # This is an Edge case
    if root.left is None and root.right is None:
        return root.val
    return root.val + max(max_path_sum(root.left), max_path_sum(root.right))
```

#### No need to check for node presence for initiating the recursive call
In tree problems there will be an obvious base case to of what to do when the node is None.</br>
So, you no need to do any of the below checks.</br>
No need to check whether left node is present/not for initiaing the recursive call on left node.</br>
No need to check whether right node is present/not for initiaing the recursive call on right node.</br>
