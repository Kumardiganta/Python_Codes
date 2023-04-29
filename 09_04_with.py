with open('jerry.txt','r') as f:
    a=f.read()
with open('jerry.txt','w') as f:
    a=f.write("Me")
print(a)