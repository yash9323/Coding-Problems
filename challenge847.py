"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Pinterest.

Given an integer list where each number represents the number of hops you can make, determine whether you can reach to the last index starting at index 0.

For example, [2, 0, 1, 0] returns True while [1, 1, 0, 1] returns False.

"""

l=[2,0,2,0,2,0,2]
pos=0
while True:
    print(pos)
    if pos >= len(l) or l[pos]==0:
        print("False")
        break
    if pos == len(l)-1:
        print("True")
        break
    pos= pos + l[pos]
