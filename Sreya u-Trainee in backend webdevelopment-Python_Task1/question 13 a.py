# 13   print the following patterns
# (a)
# 	          *
#            * *
#           * * *
#          * * * *


rows = 4

for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end="")
    for j in range(1, i + 1):
        print("*", end=" ")
    print()
