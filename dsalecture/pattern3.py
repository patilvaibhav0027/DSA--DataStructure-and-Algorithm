
def printPattern(n:int):
    for i in range(n):
       for j in range(n):
          if i == n//2 or j == n//2 :
            print("*" , end="")
          else:
            print(" ", end="")
       print()

n = int(input("Enter the number"))
printPattern(n)