# Subset Sum Problem 
'''
Daily Coding Problem: Problem #1591 [Hard]
Good morning! Here's your coding interview problem for today.
This problem was asked by Google.
Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k. If such a subset cannot be made, then return null.
Integers can appear more than once in the list. You may assume all numbers in the list are positive.
For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.
'''
def subsetSum(Array,res,total,index):
    if total == 0 :
        print("Subset Found:",res)
        return True 
    if index == len(Array):
        return False 
    if Array[index] > total:
        return subsetSum(Array,res,total,index+1)
    return subsetSum(Array, res+[Array[index]], total - Array[index], index+1) or subsetSum(Array, res, total, index+1)

'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given an N by N matrix, rotate it by 90 degrees clockwise.
'''
def rotate_matrix(m):
    m.reverse()
    for r in range(len(m)):
        for c in range(r+1,len(m[0])):
            m[r][c],m[c][r] = m[c][r],m[r][c]
    return m

class Node:
    def __init__(self,val, left=None, right=None):
        self.value = val 
        self.left = left 
        self.right = right
    def __str__(self):
        return f"Node Value:{self.value}"
    
def preorder(root):
    if root is None:
        return 
    print(root.value,end=" ")
    preorder(root.left)
    preorder(root.right)

def inorder(root):
    if root is None:
        return 
    inorder(root.left)
    print(root.value,end=" ")
    inorder(root.right)

def postorder(root):
    if root is None:
        return 
    postorder(root.left)
    postorder(root.right)
    print(root.value,end=" ")
    
root = Node("a")
root.left = Node("b")
root.right = Node("c")
root.left.left = Node("d")
root.left.right = Node("e")
root.right.left = Node("f")
root.right.right = Node("g")
        
print("Preorder:")
preorder(root)
print("\n")
print("Inorder:")
inorder(root)
print("\n")
print("Postorder:")
postorder(root)
print("\n")

# Creating Trees using traversal arrays 



# Binary Tree path from root to leaf ( return Path )
'''
Good morning! Here's your coding interview problem for today.

This question was asked by Apple.

Given a binary tree, find a minimum path sum from root to a leaf.

For example, the minimum path in this tree is [10, 5, 1, -1], which has sum 15.
'''

'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Pivotal.

Write an algorithm that finds the total number of set bits in all integers between 1 and N.
'''
n = 25
count = 0 
while n:
    count += n & 1
    n >>= 1
print(count)


import time 

def timed(func):
    def wrapper():
        print("here")
        s = time.time()
        func()
        e = time.time()
        print(f"{func.__name__} took {e-s} seconds.")
    return wrapper

@timed
def f():
    print("Yo")

f()

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def ff(data):
    x = Node(data[0])
    h = x
    for d in data[1:]:
        h.next = Node(d)
        h = h.next
    h.next = None
    return x
def f(x):
    h = x
    while h:
        print(h.val)
        h = h.next


def f(x):
    r = 0 
    while x:
        print(x%10)
        r = (r*10)  + x % 10 
        x //= 10 
    print(r)

f(123)