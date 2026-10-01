#write a progrm for armstrong no.

num=int(input("enter number:"))
n=num
sum=0
p=len(str(num))



while num > 0:
    sum+=(num%10)**p
    num//=10
    
if n==sum:
    print("number is armstrong")




    