# program to find the Project Euler Largest palindrome product

palindrome_list=[]
for i in range(100,1000):
    for j in range(100,1000):
        a = i * j
        if(str(a) == str(a)[::-1] and a not in palindrome_list ):
            palindrome_list.append(a)
palindrome_list.sort() 
length=len(palindrome_list)

n = int(input())
for _ in range(n):
    a = int(input())
    for i in range(length - 1, -1, -1):
        if palindrome_list[i] < a:
            print(palindrome_list[i])
            break
