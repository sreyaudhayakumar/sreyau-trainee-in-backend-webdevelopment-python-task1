# Find the factorial of a number taken as input using for loop

number=int(input("enter the number to find factorial :"))
fact=1
for i in range(1,number+1):
    fact=fact*i
print("factorial of number",number,"is",fact)