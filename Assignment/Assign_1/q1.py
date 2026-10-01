#  Calculate Array Sum: 
# Write a program to accept N integers into an array and 
# calculate and display the sum of all the elements. 

n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    arr.append(int(input("enter number: ")))
sum=0
for i in arr:
    sum += i
print("sum of all numbers is ", sum)