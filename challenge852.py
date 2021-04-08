"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

Given a circular array, compute its maximum subarray sum in O(n) time. A subarray can be empty, and in this case the sum is 0.

For example, given [8, -1, 3, 4], return 15 as we choose the numbers 3, 4, and 8 where the 8 is obtained from wrapping around.

Given [-4, 5, 1, 0], return 6 as we choose the numbers 5 and 1

"""

def whatever(a):
    longg=0
    for i in range(0,len(a)):
        if a[i] < 0:
            continue
        pos=i
        sum=0
        while True:
            if a[pos]<0:
                break
            sum=sum+a[pos]
            pos=pos+1
            if pos==len(a):
                pos=0         
        if sum > longg:
            longg=sum
    return longg

a=[8,-1,3,4]
print(a,"->",whatever(a))

a=[-4, 5, 1, 0]
print(a,"->",whatever(a))
