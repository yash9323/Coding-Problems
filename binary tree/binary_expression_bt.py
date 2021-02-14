'''
Evaluating a binary expression tree
'''

class Node:
    def __init__(self,val,left=None,right=None):
        self.val=val
        self.right=right
        self.left=left

def process(op,x,y):
    if op =='+':
        return x+y
    if op == '*':
        return x*y
    if op == '-':
        return x-y
    if op == '/':
        return x/y

def isleaf(root):
    return root.left is None and root.right is None

def eval(root):
    if root is None:
        return 0
    if isleaf(root):
        return int(root.val)
    x=eval(root.left)
    y=eval(root.right)
    return process(root.val,x,y)

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

    print("The expected ans is : 100 ")

    print("The binary tree was calculated , The ans is :",eval(root))
