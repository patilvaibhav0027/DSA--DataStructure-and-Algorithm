#sum of all natural numbers till 5 | n=5, sum=1^3+ till 5^3  | sum[n+(n=1)/2]^2

sum=0
n=int(input("input numbers : "))

sum=((n*(n+1))//2)**2
print(sum)