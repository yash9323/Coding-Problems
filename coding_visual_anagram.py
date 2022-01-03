#Coding Problem Visual Anagram 
#method 1 
s1 = "dangerr"
s2 = "garden"
count = 0 
sld={}
skd={}

for i in s1:
    if i not in sld:
        sld[i]=count+1
        count=0
    else:
        sld[i]+=1

for j in s2:
    if j not in skd:
        skd[j]=count+1
        count=0
    else:
        skd[i]+=1

print(sld,skd)
if sld==skd : 
    print("true strings are anagram method 1 ") 
else:
    print("false strings are not anagram  ")

#method 2 easy way time complexity O( N LOG N )
if sorted(s1)==sorted(s2):
    print("true strings are anagram ") 
else:
    print("negative ")
