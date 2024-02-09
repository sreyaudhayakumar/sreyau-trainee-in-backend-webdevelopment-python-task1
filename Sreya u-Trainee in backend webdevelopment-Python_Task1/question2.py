#Python Program to replicate bank transaction: min balance 500, ask user to the amount to withdraw, 
#print the balance amount after withdrawal, if user enters an amount greater than balance: print:: insufficient balance. 
#if balance is below 500 print an alert message : your account balance is "available_balance", Please  keep your account balance above Rs.500 to avoid unwanted charges.

min_balance=500
withdrawal_amount=int(input("enter the amount to withdraw:"))
remaining_bal=min_balance-withdrawal_amount

if withdrawal_amount>500:
    print("insufficient balance")
    
else:
    if withdrawal_amount<=500:
        remaining_bal=min_balance-withdrawal_amount
        print("balance amount after withdrawal is ",remaining_bal)
        print("your account balance is",remaining_bal,"please keep your account balance above RS.500 to avoid upwanted charges")