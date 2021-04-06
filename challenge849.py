"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Apple.

A Collatz sequence in mathematics can be defined as follows. Starting with any positive integer:

if n is even, the next number in the sequence is n / 2
if n is odd, the next number in the sequence is 3n + 1
It is conjectured that every such sequence eventually reaches the number 1. Test this conjecture.

Bonus: What input n <= 1000000 gives the longest sequence?

"""
from functools import lru_cache 

@lru_cache()
def yo():
    l=[]
    longest=0
    sec=0
    for j in range(2,1000000):
        l.append(j)
        print("for series starting with ",j)
        for i in l:
            if i==1:
                break
            if i%2==0:
                l.append(int(i/2))
            else:
                l.append(int((3*i) + 1))
        if len(l)>longest:
            longest=len(l)
            sec=j
        l=[]

    print(longest,sec)

yo()
