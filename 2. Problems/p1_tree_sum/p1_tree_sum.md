<ins>Problem:</ins> </br>
Write a function, tree_sum, that takes in the root of below binary tree that contains number values.</br> 
The function should return the total sum of all values in the tree.
![image](https://github.com/user-attachments/assets/51aadd74-d517-4577-a161-d6379521c0c3)
<ins>Solution:</ins> </br>
First thing to do it, assume the Tree as below. Doing so will make it easy to understand how the recursive code works.
![image](https://github.com/user-attachments/assets/b1a0fb38-14fe-41ce-bf35-f4dcea24a05e)
<ins>Base case:</ins> </br>
--> Input is "root node" of tree. "root node" means, not a single node. You are sending root node of the tree, by using which whole tree can be travelled.</br>
--> So, smallest input means there is no tree --> Which means "root node is None". Sum of all nodes of such a tree is "0".</br>
--> So, Base case is:
```python
def tree_sum(root):
  if root is None:
    return 0
```
![image](https://github.com/user-attachments/assets/cbb85e06-3d58-48ee-8e1c-705d27e14552)
<ins>Recursive step:</ins> </br>
When values start returning from Base case, if we do below calculation, then will end up with total sum when we reach the root node.</br>
Sum of tree upto current node = value of current node + returned value from the left tree of current node + returned value from the right tree of current node
