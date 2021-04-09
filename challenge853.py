"""

Good morning! Here's your coding interview problem for today.

Find an efficient algorithm to find the smallest distance (measured in number of words) between any two given words in a string.

For example, given words "hello", and "world" and a text content of "dog cat hello cat dog dog hello cat world", 

return 1 because there's only one word "cat" in between the two words.

"""

def eff(l):
    sm_len=0
    iter=0
    for i in range(0,len(l)):
        if l[i]!="hello":
            continue
        pos=i
        count=0
        iter=iter+1
        while True:
            pos=pos+1
            count=count+1
            if l[pos+1]=="world":
                break  
        if iter==1:
            sm_len=count
        if count<sm_len:
            sm_len=count

    print(" the smallest distance (measured in number of words) between any \n two given words in a string is :",sm_len)

#getting the words from the string to find the minimum distance 
strr="dog cat hello cat dog dog hello cat hello cat dog dog hello cat world "
word=""
l=[]
for words in strr:
    if words==" ":
        l.append(word)
        word=""
    else:
        word+=words
print(l)
eff(l) #using the function to get the minimum distance 
