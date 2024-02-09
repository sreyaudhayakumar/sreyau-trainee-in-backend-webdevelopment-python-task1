#Write python programs , which accept two inputs and perform the following arithmetic operations
	#    i)    Addition (+)
       # ii)   Subtraction (-)
        #iii)  Multiplication (*)
        #iv)   Division (/)
       # v)    Modulus (%)
        #vi)   Exponentiation (**)
        #vii)  Floor Division (//)  

input1 = int(input("Enter a value: "))
input2 = int(input("Enter another value: "))
operator = input("Enter the operator (+, -, *, /, %, **, //): ")

if operator == '+':
    print("Addition of two numbers:", input1 + input2)
elif operator == '-':
    print("Subtraction of two numbers:", input1 - input2)
elif operator == '*':
    print("Multiplication of two numbers:", input1 * input2)
elif operator == '/':
    print("Division of two numbers:", input1 / input2)
elif operator == '%':
    print("Modulus of two numbers:", input1 % input2)
elif operator == '**':
    print("Exponentiation of two numbers:", input1 ** input2)
elif operator == '//':
    print("Floor division of two numbers:", input1 // input2)
else:
    print("Invalid operator")
