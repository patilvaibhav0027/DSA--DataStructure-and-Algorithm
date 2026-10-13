# 4. Search an Element: 
# Write a program to accept N integers into an array and search for a given number. 
# Display an appropriate message indicating whether the number is present in the array or not 
# and also display its position. 


n=int(input("enter number of elements: "))

arr=[]

for i in range(n):
    arr.append(int(input("enter numbers: ")))

x=(int(input("enter searching number:")))
for i in range(n):
    if arr[i]==x:
        print("found ")
        break
else:
    print("not found")