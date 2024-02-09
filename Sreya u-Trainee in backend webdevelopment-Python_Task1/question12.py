# Print first 10 fibonacci numbers using 'for' and 'while' loops
# for loop
number = 10
n1 = 0
n2 = 1

if number <= 0:
    print("Please enter a number greater than 0")
else:
    for i in range(number):
        print(n1, end=" ")
        nth = n1 + n2
        n1 = n2
        n2 = nth

print()  

# while loop

number = 10
n1 = 0
n2 = 1
i = 0


if number <= 0:
    print("Please enter a number greater than 0")
else:
    while i < number:
        print(n1, end=" ")
        nth = n1 + n2
        n1 = n2
        n2 = nth
        i += 1

print() 
