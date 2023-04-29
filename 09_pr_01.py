f=open('C:\\Users\\DIGANTA\\WORKSPACE\\PYTHON\\poems.txt')
t=f.read()
if 'twinkle' in t:
    print("Twinkle is present")
else:
    print("Twinkle is not present")
f.close()