
//Program to implement Project Euler Even Fibonacci numbers in python 
import sys
def even_fibo(n):
    l=[1,1]
    i=1
    sume=0
    while( l[i] <= n ) :
        ab=l[i]+l[i-1]
        l.append(ab)
        i=i+1
    l.pop()
    for i in l:
        if(i%2==0):
            sume=sume+i
    return sume


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    ans =even_fibo(n)
    print(ans)
    

