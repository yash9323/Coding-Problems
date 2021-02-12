#inorder traversal of the binary tree 
from collections import deque
class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right

def inorder_r(root):
    if root is None :
        print("The binary tree is empth ,please add some nodes!!")
    if root.left:
        inorder_r(root.left)
    print(root.data,end=" - ")
    if root.right:
        inorder_r(root.right)
    

def inorder_i(root):
    if root is None :
        print("The binary tree is empth ,please add some nodes!!")
    s=deque()
    curr = root
    while s or curr:
        if curr:
            s.append(curr)
            curr=curr.left
        else:
            curr=s.pop()
            print(curr.data,end=" - ")
            curr=curr.right

   
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

    print("\n The In Order Traversal of the binary tree through recursively is ")
    inorder_r(root)
    print("\n The In Order Traversal of the binary tree through iteration is ")
    inorder_i(root)
