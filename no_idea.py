'''
There is an array of  integers. There are also  disjoint sets,  and , each containing  integers. You like all the integers in set  and dislike all the integers in set . Your initial happiness is . For each  integer in the array, if , you add  to your happiness. If , you add  to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.
Note: Since  and  are sets, they have no repeated elements. However, the array might contain duplicate elements.
'''
n,m=map(int,input().split())
l=list(map(int,input().strip().split()))[:n]
A=list(map(int,input().strip().split()))[:m]
B=list(map(int,input().strip().split()))[:m]
happiness = 0
A=set(A)
B=set(B)
for i in l:
    if i in A:
        happiness+=1
    if i in B:
        happiness-=1
print(happiness)
