#level order traversal of a binary tree 

from collections import deque
class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.right=right
        self.left=left

def levelordertraversal(root):
    if root is None:
        print("No nodes in tree ")
    
    q=deque()
    q.append(root)

    while q :
        curr=q.popleft()
        print(curr.data)
        if curr.left:
            q.append(curr.left)
        if curr.right:
            q.append(curr.right)
        

if __name__ ==  "__main__":
    root=Node(1)
    root.left=Node(2)
    root.right=Node(3)
    root.left.left=Node(4)
    root.left.right=Node(5)
    
    levelordertraversal(root)
