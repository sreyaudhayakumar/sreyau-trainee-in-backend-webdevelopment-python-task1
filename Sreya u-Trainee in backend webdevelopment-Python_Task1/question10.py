# Find the sum of all even numbers between the range given by user

number=int(input("enter the range of number :"))
sum=0
for i in range(2,number+1):
    if i%2 == 0:
     sum=sum+i
print("Sum of all even numbers between", 2, "and", number, "is", sum)
