"""
Project Euler Problem 4
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""

import time 
l=[]
maxx=0

def ispanlindrome(n):
    l=str(n)
    if l==l[::-1]: return True

start_time=time.time()
for i in range(999,100,-1):
    for j in range(999,100,-1):
        a=i*j
        if ispanlindrome(a):
            if a>maxx:
                maxx=a
                
print(maxx)
print(time.time()-start_time)
