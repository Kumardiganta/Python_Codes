num = int(input("Enter the no: \n"))
prime = True
for i in range(2,num):
    if(num%i == 0):
        prime = False
        break
if prime:    
    print("This Number " + str(num) + " is a Prime No.")
else:
    print("This Number " + str(num) + " is not a Prime No.")