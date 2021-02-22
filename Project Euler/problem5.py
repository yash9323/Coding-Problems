"""
Project Euler Problem 5
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

#Approach 1 :  time taken for execution is 23.85... seconds 
from functools import lru_cache
import time 
@lru_cache()
def compute_lcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

start_time=time.time()
lcm=1
for i in range(1,21):
    lcm=compute_lcm(lcm,i)
print("{} is the least common multiple of all the nos between 1-20".format(lcm))
print("approach 1 Execution took {} seconds ".format(time.time()-start_time))

#Approach 2:
import math 
def lcm(n):  
    ans = 1
    for i in range(1, n + 1):  
        ans = int((ans * i)/math.gcd(ans, i))        
    return ans  
start_time=time.time()
print (lcm(20))  
print("approach 2 Execution took {} seconds ".format(time.time()-start_time))
