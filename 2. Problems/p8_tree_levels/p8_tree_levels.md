<ins>Logic:</ins></br>
Until now, we used to push only the node into Queue/Stack.</br>
But, this time we need to push level of the corresponding node also.</br>
So, push a tuple (node, level)</br>
Because of doing so, whenever we are working on a node, we know what's the level of that node</br>
and also the child nodes of that node will have level = current node level + 1.
![image](https://github.com/user-attachments/assets/b5314e6a-5371-491c-83d5-d2c572c29dd7)
