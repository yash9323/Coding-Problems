from collections import deque 

class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.right=right
        self.left=left

#height of a binary tree using recurssion    
def height_r(root):
    if root is None :
        return 0 
    
    return 1+ max(height_r(root.left),height_r(root.right))

#height of a binary tree using iteration
def height_i(root):
    if root is None :
        return 0 
    
    q=deque()
    q.append(root)

    ht=0
    while q :
        size=len(q)
        while size>0:
            curr=q.popleft()
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
            size=size-1
        ht=ht+1
    return ht 
                

if __name__== "__main__":
    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left=Node(4)
    root.left.right=Node(5)
    root.left.left.left=Node(9)
    root.left.left.right=Node(10)
    root.right.left=Node(6)
    root.right.right=Node(7)
    root.right.left.right=Node(8)

    print("The Height of the binary tree using recurcision is ",height_r(root))

    print("The Height of the binary tree using iteration is ",height_i(root))
