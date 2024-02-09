# Python program to print all even/odd numbers in the range given by user


number=int(input("enter the range"))
for num in range(1,number+1):
    if num%2 == 0:
        print(num)
