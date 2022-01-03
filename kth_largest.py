#Coding Problem kth largest number
#to find the kth largest element 
#You can either sort the array and return the target index 
#or you could iterate through and then remove the three largest elements 

arr=[4,2,9,7,5,6,7,1,3]
trgt=4
arr=sorted(arr,reverse=True)
print(arr)
print(arr[trgt-1])
