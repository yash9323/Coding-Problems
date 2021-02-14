#Preorder traversal of the binary tree using recurssion and interation 
from collections import deque
class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right

def preorder_r(root):
    if root is None :
        print("There are no nodes in the binary tree , so please go add some !!")
    print(root.data,end=" ")
    if root.left:
        preorder_r(root.left)
    if root.right:
        preorder_r(root.right)    

def preorder_i(root):
    if root is None:
        print("There are no nodes in the binary tree , so please go add some !!")
    s=deque()
    s.append(root)
    while s :
        curr=s.pop()
        print(curr.data,end=" ")
        if curr.right:
            s.append(curr.right)   
        if curr.left:
            s.append(curr.left) 
        
    
if  __name__ == "__main__":
    '''
                 1
                / \
               /   \
              2     3
             /     /  \
            4     5    6 
                 /\
                7  8     
    '''
    root=Node(1)
    root.left=Node(2)
    root.left.left=Node(4)
    root.right=Node(3)
    root.right.right=Node(6)
    root.right.left=Node(5)
    root.right.left.left=Node(7)
    root.right.left.right=Node(8)

    print("\n The Pre Order Traversal of the binary tree through recursively is ")
    preorder_r(root)
    print("\n The pre order traversal of the binary tree using iteration is :")
    preorder_i(root)
