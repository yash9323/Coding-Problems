#Printing all the paths from root to all Leaf Nodes

from collections import deque

class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

def isleaf(node):
    return node.left is None and node.right is None 

def Paths(node,path):
    if node is None:
        return 
    path.append(node.val)
    if isleaf(node):
        print(list(path))
    Paths(node.left,path)
    Paths(node.right,path)
    path.pop()

def printRootToLeafPath(root):
    path=deque()
    Paths(root,path) 
    
if __name__ == "__main__":

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

    print("All the paths from root to leaf nodes are ")
    printRootToLeafPath(root)
