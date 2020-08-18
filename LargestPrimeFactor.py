//program to solve the Project Euler Largest prime factor
import sys
import math
def primefactors(n):
    l=[]
    while n%2==0:
        l.append(2)
        n=n/2
    
    for i in range(3,int(math.sqrt(n)+1),2):
        while n%i==0:
            l.append(int(i))
            n=n/i
    if n>2:
        l.append(int(n))

    return max(l)

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    print(primefactors(n))
