import random

def game(comp,you):
    pass

print("Comp  Turn: Snake(s) Water(w) or Gun(g)?")
randNo=random.randint(1,3)
if randNo==1:
    comp='s'
elif randNo==2:
    comp='w'
elif randNo==3:
    comp='g'
you=input("Your Turn: Snake(1) Water(2) or Gun(3)?")

# game()