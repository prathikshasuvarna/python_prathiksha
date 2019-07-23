"""1.	Write a program to accept a number and determine whether it is a prime number or not."""
num=int(input("enter the number:"))
flag=1
if num<2:
    flag=0
else:
    for i in range(2,(num//2+1)):
        if num % i == 0:
           flag=0
           break
        else:
            flag=1
if flag==0:
    print(f"{num} is not a prime number")
else:
    print(f"{num} is a prime number")




