# Find the sum of all odd numbers between the range given by user using while loop

number=int(input("enter the range of number: "))
sum=0
i=1
while i<number:
    if i% 2 == 1:
        sum=sum+i
    i=i+1
print("sum of all odd number between the range is",sum)