#checking if a binary tree is skewed or not !!

class Node:
    def __init__(self,data,left=None,right=None):
        self.data=data
        self.right=right
        self.left=left

def isskwed(root):
    if root is None:
        return True
    
    if root.left and root.right:
        return False
    
    return isskwed(root.left) and isskwed(root.right)


if __name__ == "__main__":
    root=Node(1)
    root.left=Node(2)
    root.right=Node(10)
    root.left.right=Node(3)
    root.left.right.left=Node(4)
    root.left.right.left.right=Node(5)

    if isskwed(root):
        print("The binary tree is skewed")
    else:
        print("the binary tree is not skwed")
