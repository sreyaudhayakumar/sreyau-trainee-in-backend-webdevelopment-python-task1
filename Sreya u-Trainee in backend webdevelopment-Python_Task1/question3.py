#Print the greatest of the 3 numbers taken as input, print equal if all three numbers are the same

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
third_number = int(input("Enter the third number: "))

if first_number > second_number and first_number > third_number:
    print("The greatest number is", first_number)
elif second_number > third_number and second_number>first_number:
    print("The greatest number is", second_number)
elif first_number==second_number==third_number:
    print("All three are equal")
else:
    print("The greatest number is",third_number)
