# for a in range(5,0,-1):
#     for b in range(1,a+1):
#         print("#",end=' ')
#     print(" ")
import os
os.system('cls')
def printpy(n):
    # outer loop for number of rows
    #n in this case
    for i in range(0,n):
        # inner loop for number of columns
        # values change according to the outer loop
        for j in range(0,i+1):
            # printing @ 
            print("#",end=" ")
            # printing line after each row
        print(" ")

n=5
printpy(n)