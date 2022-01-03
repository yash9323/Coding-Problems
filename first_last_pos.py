#Coding Problem fIRST AND LAST POSITION PROBLEM 
#let the idexing of the array be from 1 

a=[12,22,25,65,84,7,23,45,654,98,12,6,5,9,3]
trgt=7
if trgt not in a :
    print("[-1,-1")
else:
    ans=[]
    first=a.index(trgt) + 1 
    last=len(a)- a[-1::-1].index(trgt)
    ans.append(first)
    ans.append(last)
    
print(ans)


