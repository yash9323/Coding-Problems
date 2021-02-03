"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Palantir.

Write a program that checks whether an integer is a palindrome. 
For example, 121 is a palindrome, as well as 888. 678 is not a palindrome. Do not convert the integer into a string.
"""

print("Enter the no to check if it is palindrome !!! ")
n=int(input())
no=n
rev=0
while(n>0):
    ans=n%10
    rev=rev*10+ans
    n=n//10

if(rev==no):
    print("the no is palindrome")
else:
    print("the no is not palindrome")

