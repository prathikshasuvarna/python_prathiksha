"""6.	Write a program to accept a number from the user; then display the reverse of the entered number.
(Example: Entered number = 12345; Reversed number = 54321)"""

n=int(input("enter a number:"))
rev=0
temp=n
while temp!=0:
    rev=rev*10+(temp%10)
    temp=temp//10
if rev==n:
    print(f"{n} is a palindrome")
else:
    print(f"{n} is not a palindrome")