<ins>Base case 1:</ins></br>
While you are exploring the tree, what needs to be returned when you found Target?</br>
![image](https://github.com/user-attachments/assets/0bbcd916-01d2-4194-9573-4a4afd89aa69)
```python
def path_finder(root, target):
  if root.val == target:
    return [ root.val ]
```
<ins>Base case 2:</ins></br>
What's the result of problem, for smallest input?</br>
None.</br> 
Why None?</br> 
The smallest input it self is the complete problem until that node.</br>
When there is no root node --> It means there is no tree --> When there is no tree, there is no path --> Which means, the path until that node is None. 
![image](https://github.com/user-attachments/assets/5292a1d6-f5a5-435b-9274-d92b089f33d5)
```python
def path_finder(root, target):
  if root is None:
    return None
  
  if root.val == target:
    return [ root.val ]
```
<ins>Recursive Step:</ins></br>
Once you have analyzed all the base cases, then think about what to be done with these base case vallues returned while we moving up, so that we end up in final result.</br>
<ins>What to do when both root.left & root.right return None?</ins>
![image](https://github.com/user-attachments/assets/8980b7b6-e811-49eb-856c-9ba06009b498)
```python
return None
```
<ins>What to do when either left node return [root.val] (or) right node return [root.val]?</ins>
![image](https://github.com/user-attachments/assets/c8238e6a-a95a-4263-9c2c-bc2585f03832)
```python
left_path = path_finder(root.left, target)
if left_path is not None:
  return [ root.val, *left_path ]

right_path = path_finder(root.right, target)
if right_path is not None:
  return [ root.val, *right_path ]
```
<ins>Final solution</ins>
```python
def path_finder(root, target):
  if root is None:
    return None
  
  if root.val == target:
    return [ root.val ]
  
  left_path = path_finder(root.left, target)
  if left_path is not None:
    return [ root.val, *left_path ]
  
  right_path = path_finder(root.right, target)
  if right_path is not None:
    return [ root.val, *right_path ]
  
  return None
```
