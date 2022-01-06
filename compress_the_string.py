'''
In this task, we would like for you to appreciate the usefulness of the groupby() function of itertools . To read more about this function, Check this out .
You are given a string . Suppose a character '' occurs consecutively  times in the string. Replace these consecutive occurrences of the character '' with  in the string.
'''
import itertools as t

S = input()
groups=[]
uniquekeys=[]
output=""

for k,g in t.groupby(S):
    groups.append(list(g))
    uniquekeys.append(k)
    
for i in groups:
    output+="("+str(len(i))+", "+str(i[0])+")"+" "
 
print(output)
