"""2.	Write a program to accept a number “n” from the user; then display the sum of the following series:
1 + 1/2 + 1/3 + ……. + 1/n"""

n=int(input("enter the value of n"))
res=1
for i in range(2,n+1):
    res+=1/i
print(f"sum of {n} following series:{res}")
