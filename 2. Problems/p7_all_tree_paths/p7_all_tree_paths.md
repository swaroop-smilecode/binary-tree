<ins>Base case 1:</ins></br>
When you hit the leaf node, that's where you should start collecting the node values inside an list</br>
So, hitting the leaf node is base case.
![image](https://github.com/user-attachments/assets/b76ede7a-cc84-423b-bd30-8c6de0aaa069)
```python
def all_tree_paths(root):
  if root.left is None and root.right is None:
      return [[root.val]]
```
<ins>Base case 2:</ins></br>
What should be returned, when we hit node None?</br>
node None itself is an Tree</br>
What are the paths of such a Tree?</br>
No paths, which means [ ]
![image](https://github.com/user-attachments/assets/78c05ead-0570-40ba-a751-21ea29ba0e75)
```python
def all_tree_paths(root):
  if root is None:
    return []
  if root.left is None and root.right is None:
    return [[root.val]]
```
<ins>Recursive case:</ins></br>
What should you do with the returned values?
![image](https://github.com/user-attachments/assets/80c2f030-feaf-463d-9c56-936ae6524de0)
