"""
Project Euler Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
Find the sum of all the primes below two million.

"""

from functools import lru_cache

@lru_cache()
def isprime(num):
    for j in range(3,num,2):
        if (num%j) == 0:
            return False
            break
    return True

@lru_cache()
def sum_prime(n):
    prime=[2,3,5,7]
    for i in range(9,n,2):
        if isprime(i):
            prime.append(i)
    print(prime)
    return sum(prime)

print("The sum of the prime nos is :",sum_prime(2000000))        
