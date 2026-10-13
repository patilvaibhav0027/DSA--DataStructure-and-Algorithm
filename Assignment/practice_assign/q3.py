# 3. Count Even and Odd Numbers: 
# Write a program to accept N integers into an array 
# and count and display the number of even and odd elements present in the array


n=int(input("enter number of elements:"))

arr=[]
even=[]
odd=[]

for i in range(n):
    arr.append(int(input("enter number: ")))

even_count = 0
odd_count = 0

for n in arr:
    if n % 2 == 0:
        even_count +=1
        even.append(n)
        print(even)
        
    else:
        odd_count +=1
        odd.append(n)
        print(odd)
        
print("Number of even: ", even_count)
print("Number of odd: ", odd_count)        
