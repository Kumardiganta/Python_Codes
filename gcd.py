n1=int(input("enter 1st no: "))
n2=int(input("enter 2nd no: "))
loop=True
while loop:
    if n1==n2:
        print(f"GCD:{n1}")
        loop=False
    elif n1>n2:
        n1 -= n2
    else:
        n2 -= n1