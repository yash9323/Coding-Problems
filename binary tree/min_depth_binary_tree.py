# finding the minimum depth of a binary tree 

from collections import deque

class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.left=left
        self.right=right
    
class qnode:
    def __init__(self,node=None,depth=None):
        self.node=node
        self.depth=depth

def isleaf(node):
    return node.left is None and node.right is None 

def mindepth(root):
    if root is None:
        return 0

    q=deque()
    q.append(qnode(root,1))

    while q :
        front=q.popleft()
        node=front.node
        depth=front.depth

        if isleaf(node):
            return depth
        
        if node.left:
            q.append(qnode(node.left,depth+1))
        
        if node.right:
            q.append(qnode(node.right,depth+1))
        

if __name__ == "__main__":
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

    print(" the minimum depth of the binary tree is : ",mindepth(root))
