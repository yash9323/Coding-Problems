# Neet Code Trees 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 226 Invert Binary Tree 
def invertTree(root):
    if root == None:
        return root 
    invertTree(root.left)
    invertTree(root.right)
    root.left,root.right = root.right,root.left 
    return root 

# 104 Maximum Depth of Binary Tree 
def maxDepth(root):
    def f(root,d):
        if root == None:
            return d
        return max(f(root.left,d + 1),f(root.right,d + 1))
    return f(root,0)

# 100 Same Tree 
def isSameTree(p,q):
    if p == None and q == None:
        return True 
    if not p or not q:
        return False 
    return p.val == q.val and isSameTree(p.left,q.left) and isSameTree(p.right,q.right)

# 110 Balanced Binary Tree 
def isBalanced(root):
    if root == None:
        return True 
    def d(root):
        return 0 if root==None else 1 + max(d(root.left),d(root.right))
    l = d(root.left)
    r = d(root.right)
    return abs(l-r) < 2 and isBalanced(root.left) and isBalanced(root.right)

# 572 Subtree of Another Tree
def isSubtree(root, subRoot):
    if root == None:
        return False 
    if subRoot == None:
        return True 
    if root.val == subRoot.val:
        if isSameTree(root,subRoot):
            return True 
    return isSubtree(root.left,subRoot) or isSubtree(root.right,subRoot)   

# 543 Diameter of a Binary Tree
def diameterOfBinaryTree(root):
    d = 0 
    def f(root):
        if root == None:
            return -1 
        l = f(root.left)
        r = f(root.right)
        d = max(d,2+l+r)
        return 1 + max(l,r)
    f(root)
    return d

# 102 Binary Tree Level Order Traversal 
def levelOrder(root):
    r = []
    def f(rr,l):
        if rr == None:
            return 
        if len(r) <= l:
            r.append([])
        r[l].append(rr.val)
        f(rr.left, l + 1)
        f(rr.right, l + 1)
    f(root,0)
    return r 

# 1448 Count Good Nodes in a Binary Tree 
def goodNodes(root):
    gn = 0 
    def f(root,pm):
        if root == None:
            return 
        if root.val >= pm:
            gn += 1
            pm = root.val
        f(root.left,pm)
        f(root.right,pm)
    f(root,float("-infinity"))
    return gn

# 199 Binary Tree Right Side View 
def rightSideView(root):
    res = []
    def f(r,d):
        if r == None:
            return 
        if len(res) == d:
            res.append(r.val)
        f(r.right,d+1)
        f(r.left,d+1)
    f(root,0)
    return res

# 235 Lowest common Ancestor of a binary search tree 
def lowestCommonAncestor(root, p, q):
    def f(r,s,p):
        if r == None:
            return 
        if r.val == s.val:
            p.append(r)
            return p 
        l = f(r.left,s,p+[r])
        if l :
            return l 
        r = f(r.right,s,p+[r])
        return r 
    pp = f(root,p,[])
    qq = f(root,q,[])
    i = min(len(pp)-1,len(qq)-1)
    while i >= 0:
        if pp[i].val == qq[i].val:
            return pp[i]
        i -= 1

# 98 validate Binary Search Tree 
def isValidBST(root):
    def f(r,mn,mx):
        if r == None:
            return True 
        if not (mn < r.val < mx):
            return False 
        return f(r.left,mn,r.val) and f(r.right,r.val,mx)
    return f(root,float("-infinity"),float("infinity"))

# 124 Binary tree Maximum Path Sum 
def maxPathSum(root):
    m = -float("inf")
    def f(r):
        if r == None:
            return 0 
        ll = f(r.left)
        rr = f(r.right)
        if ll < 0: ll = 0 
        if rr < 0: rr = 0 
        m = max(m,r.val+ll+rr)
        return r.val + max(ll,rr)
    f(root)
    return m

# 230 kth Smallest Element in a BST 
def kthSmallest(root, k) :
    res = []
    def f(r):
        if r == None:
            return 
        f(r.left)
        res.append(r.val)
        if len(res) > k:
            return res[k-1]
        f(r.right)
    f(root)
    return res[k-1]

# 105 Construct Binary Tree from Preorder and Inorder Traversal 
def buildTree(preorder, inorder):
    if not preorder or not inorder:
        return 
    r = TreeNode(preorder[0])
    m = inorder.index(preorder[0])
    r.left = buildTree(preorder[1:m+1],inorder[:m])
    r.right = buildTree(preorder[m+1:],inorder[m+1:])
    return r 

# 297 Serialize and Deserialize a Binary Tree 
class Codec:
    def serialize(self, root):
        def f(r):
            if r == None:
                self.e.append("null")
                return 
            self.e.append(str(r.val))
            f(r.left)
            f(r.right)
        self.e = []
        f(root)
        return ','.join(self.e)
        
    def deserialize(self, data):
        def f():
            if data[self.i] == "null":
                self.i += 1
                return None
            r = TreeNode(int(data[self.i]))
            self.i += 1
            r.left = f()
            r.right = f()
            return r
        data = data.split(',')
        self.i = 0
        return f()
