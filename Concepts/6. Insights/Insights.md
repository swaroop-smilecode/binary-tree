#### Initiating recursive calls on left node & right node
- If you are initiating recurisve calls in DFS, then it will be like
  ```python
  recursive_call(root.left)
  recursive_call(root.right)
  ```
- If you are initiating recurisve calls in BFS, then it will be like
  ```python
  recursive_call(currrent.left)
  recursive_call(current.right)
  ```

#### Problems that has special base cases
`max path sum` problem
```python
def max_path_sum(root):
    if root is None:
        return float("-inf")
    # This is an Edge case
    if root.left is None and root.right is None:
        return root.val
    return root.val + max(max_path_sum(root.left), max_path_sum(root.right))
```
`how high` problem
```python
def how_high(node):
    if node is None:
        return -1
```

#### `all_tree_paths` problem
There are 2 things you need to be careful about.
1. Base cases
```python
def _all_tree_paths(root):
    if root is None:
        return []

    if root.left is None and root.right is None:
        return [[root.val]]
```
2. You will get answer in reverse way. To correct it, do as below:
```python
def all_tree_paths(root):
    paths = _all_tree_paths(root)
    for path in paths:
        path.reverse() 
    return paths
```

#### No need to check for node presence for initiating the recursive calls in DFS
- In tree problems there will be an obvious base case of what to do when the node is None.</br>
  So, you no need to do any of the below checks.</br>
  No need to check whether left node is present/not for initiaing the recursive call on left node.</br>
  No need to check whether right node is present/not for initiaing the recursive call on right node.</br>
- Where as there will no such base case when you are implementing the BFS algorithm.</br>
  Hence, you need to check for node presence before initiating the recursive call.

#### When to use DFS & when to use BFS?
If the problem is asking for `closest path` / `smallest path`, then go for `BFS`, else `DFS`.

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
#### If you are implementing BFS algorithm, then remember these methods:
```python
popleft()
append()
```
