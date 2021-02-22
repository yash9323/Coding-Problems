"""
Project Euler Problem No 6
The sum of the squares of the first ten natural numbers is,

The square of the sum of the first ten natural numbers is,

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .
3025-385
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""
"""
The sum of n numbers is given by n*n+1/2
The sum of squares of n numbers is given by (n*n+1*2n+1)/6
"""
n=100
sum_of_the_squares=(n)*(n+1)*(2*n+1) /6
square_of_the_sum=(n*(n+1)/2)**2
print("The Difference between the sum of the squares of the first one hundred natural numbers and the square of the sum. is :",square_of_the_sum-sum_of_the_squares)
