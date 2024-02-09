# Python program to print the multiplication table of any number (number should be taken as input and user decides the end limit of the table)

number = int(input("Enter the number: "))
limit = int(input("Enter the limit: "))

for i in range(1, limit + 1):
    print(i, "*", number, "=", i * number)
