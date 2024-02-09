# Find the factorial of a number taken as input using while loop

number = int(input("enter the number to find the factorial :"))
fact =1
i=1
while i<=number:
    fact=fact*i
    i=i+1
print("factorial of ",number,"is",fact)