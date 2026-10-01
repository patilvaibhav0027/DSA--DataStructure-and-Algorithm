
num=int(input("enter a number:"))
sum=0
n=num

while(num>0):
    sum=sum*10+(num%10)
    num//10

if(n==sum):
    print("Number is Palindrome")

    