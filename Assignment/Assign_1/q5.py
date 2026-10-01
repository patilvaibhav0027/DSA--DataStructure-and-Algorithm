# 5. Reverse the Array: 
# Write a program to accept N integers into an array and display the elements in reverse order 
# without changing the original array. 

n = int(input("enter number of elements:"))

arr=[]

for i in range(n):
    arr.append(int(input("enter numbers:")))

for i in range(n-1, -1, -1):
    print(arr[i], end=" ")

#n-1 defines that n is the we are going in desending order
# this is the elemets in a list (110 28 30 47 59 65)  and indexing is (0 1 2 3 4 5 )
# n here is the 
