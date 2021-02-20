"""
Project Euler Problem 1 
If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

"""

#Approach 1 : iterations =532
list1=[]
i=3
list2=[]
j=5
while i < 1000:
    list1.append(i)
    i+=3

while j < 1000:
    list2.append(j)
    j+=5

list3=set(list1+list2)
print(sum(list3))


#Approach 2 : Iterations :1000
total_sum = 0
for i in range(1000):
    if (i%3 == 0 or i%5 == 0):
        total_sum = total_sum+i
print (total_sum)  


#Approach 3:
"""
The sum of all numbers from 1 to n is equal to n*(n+1)/2
So the sum of all numbers less than 1000 that divides 3 is
n=333
(3*333)*(333+1)/2
So the sum of all numbers less than 1000 that divides 5 is
n=199
(5*199)*(199+1)/2
Adding the two numbers would overcount though. Since the numbers that divides both 3 and 5 would get counted twice.
The numbers that divides both 3 and 5 is precisely the numbers that divides 15
The sum of all numbers less than 1000 that divides 15 is
n=66
(15*66)*(66+1)/2
final Ans = a + b - c
"""
a=3*(999//3)*((999//3)+1)/2
b=5*(999//5)*((999//5)+1)/2
c=15*(999//15)*((999//15)+1)/2
Ans=a+b-c
print(int(Ans))
