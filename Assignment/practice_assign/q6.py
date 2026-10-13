# 6. Remove Duplicate Elements: 
# Write a program to accept N integers into an array and 
# create a new array containing only the unique elements, 
# removing all duplicate values. 

def remove_duplicate(n: list) -> list:
    arr = []
   # for i in range(len(n)):
     #  arr.append(n[i])

    for i in n:
        arr.append(i)
    return arr

# n = int(input("enter number of elements: "))

dem = [2, 5 , 75, 52, 5, 50]

remove_duplicate(dem)

for i in range(len(dem)):
   print(dem[i])



