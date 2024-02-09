# (b)	o
# 		1 2
# 		3 4 5
# 		6 7 8 9

x=0
for i in range (0,4):
    for j in range(0,i+1):
        print(x,end=" ")
        x =x+1
    print()