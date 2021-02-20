"""
Project Euler Problem 3
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 
600851475143 ?
"""
import math
import time 
def Max_Prime_Factor(n):
    l=[]
    while n%2 == 0:
        l.append(2)
        n/=2
    for i in range(3,int((math.sqrt(n)+1)),2):
        if n%i==0:
            l.append(i)
            n/=i
    if n>2:
        l.append(n)
    return max(l)

n=float(input("Enter the No to get the max prime factor:"))
start_time=time.time()
print(Max_Prime_Factor(n))
print("The time taken to execute in seconds is :",time.time()-start_time)
