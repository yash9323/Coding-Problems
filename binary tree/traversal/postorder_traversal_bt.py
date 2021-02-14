#post order traversal of the binary tree using recurssion and iteration 

from collections import deque
class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.right=right
        self.left=left

def postorder_r(root):
    if root is None:
        return 0
    if root.left:
        postorder_r(root.left)
    if root.right:
        postorder_r(root.right)
    print(root.val,end=" -- ")

def postorder_i(root):
    if root is None:
        return 0
    q=deque()
    o=deque()
    q.append(root)
    while q:
        curr=q.pop()
        o.append(curr.val)
        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)
        
    while o:
        print(o.pop(),end=" -- ")

if __name__ == "__main__":
    """

                +
               / \
              *   *
             /\   /\ 
            5 10 5 10

    """
    root=Node('+')
    root.left=Node('*')
    root.left.left=Node(5)
    root.left.right=Node(10)
    root.right=Node('*')
    root.right.left=Node(5)
    root.right.right=Node(10)

    print("\n Post Order Traversal of the binary tree using recurssion ")
    postorder_r(root)

    print("\n Post Order Traversal of the binary tree using iteration ")
    postorder_i(root)
