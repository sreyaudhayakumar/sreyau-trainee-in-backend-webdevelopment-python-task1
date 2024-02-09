#Python program to check the number taken as an input is even or odd,print invalide input if user enters anything other than integers


try:
    number = int(input("enter a number:"))
    if number %2 == 0:
        print(number,'is even.')
        
    else:
        print(number,"is odd")
        
except ValueError:
    print("invalid input.please enter an integer")
    