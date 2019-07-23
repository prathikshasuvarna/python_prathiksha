"""4.	Write a program to accept a number “n” from the user; then display the sum of the following series:
1/2^3 + 1/3^3 + 1/4^3 + …… + 1/n^3"""
n=int(input("enter the value of n:"))
res=0
for i in range(1,n+1):
    res+=1/i**3
print(f"sum of {n} following series:{res}")

