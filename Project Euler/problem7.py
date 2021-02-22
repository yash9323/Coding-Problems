"""
Project Euler Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
we can see that the 6th prime is 13.
What is the 10 001st prime number?
"""

def isprime(num):
    for j in range(2,num):
        if (num%j) == 0:
            return False
            break
    return True

def prime(n):
    l=[2]
    i=3
    while len(l) < n:
        if isprime(i):
            l.append(i)
        i+=2
    print(l[n-1])

prime(10001)
