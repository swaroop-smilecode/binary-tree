Given the below values of tree in `inorder traversal` & `postorder traversal`, build the tree.
![image](https://github.com/user-attachments/assets/629c966c-ce30-4194-a5c6-fa8739a38f90)

### Approach
The first thing to understand is by using the values of either only inorder traversal / postorder traversal, you can't build the tree.</br>
For example; look at the below two trees. Both will result in the same values if you traverse them in inorder traversal manner</br>
But, they are different.
![image](https://github.com/user-attachments/assets/a6fde32d-eabd-40e5-b12a-3ab3938666a4)

What is `inorder traversal` & `postorder traversal`?
![image](https://github.com/user-attachments/assets/667f43e8-d73f-40c7-b23b-ad18a2c9e784)

In `Postorder traversal`, it is guaranteed that the last node we visit is the `root node`.</br>
So, will find out what is our root node from  `Postorder traversal` data.
![image](https://github.com/user-attachments/assets/35455787-0284-4a3b-b2e4-1c88374fea4d)

Once you know the value of `root node` from `postorder traversal`,</br>
Find out which one is `left node` & which one is `right node` from the `inorder traversal` data.</br>
And then finally compare did the values of `left node` & `right node` which you got from `inorder traversal` data</br>
are also getting aligned with the `postorder traversal` data.
![image](https://github.com/user-attachments/assets/879ed5e2-eff9-4898-9076-d019389dd41e)

#### Let's look at big example
![image](https://github.com/user-attachments/assets/407a13f3-78c5-4506-a7f2-4958e6fc7940)

![image](https://github.com/user-attachments/assets/67a6deee-e841-43ae-9d6c-22fdd78a7448)

![image](https://github.com/user-attachments/assets/d3846193-5d11-408a-b577-cf3f8190bb60)

Complete tree looks like below.
![image](https://github.com/user-attachments/assets/15e7f126-5238-4d86-9d60-af079a45e962)
