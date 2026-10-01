n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    arr.append(int(input("enter number: ")))

min = arr[0]
max = arr [0]
smin = arr[1] 
smax = arr[0]

for i in arr:
    if i<min:
        smin=min
        min=i
    #elif i<min and i >min:
    #     smin=i

    if i>max: 
        smax=max
        max=i
    elif i>smax and i!= max:
        smax=i
        
print("Maximum:", max )
print("Minimum:", min )
print("Second Minimum:", smin ) 
print("Second Maximum:", smax )

 

