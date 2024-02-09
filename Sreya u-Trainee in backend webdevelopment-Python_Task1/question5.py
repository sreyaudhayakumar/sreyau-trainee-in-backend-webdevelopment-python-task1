# Python program to check the score from a student ,print grades as A+ if score >= 90,A if 80 or above, B+ if 70 or above and so on... 
#  print failed if the score is below 50, if score > 100 print invalid

score=int(input("enter the score:"))
if (score>=90 and score<=100):
    print("grade is A+")
elif(score>=80 and score<=89):
    print("grade is A")
elif(score>=70 and score<=79):
    print("grade is B+")
elif(score>=60 and score<=69):
    print("grade is B")
elif(score>=50 and score<=59):
    print("grade is C+")
elif(score<50):
    print("failed")
else:
    print("invalid input")
    

