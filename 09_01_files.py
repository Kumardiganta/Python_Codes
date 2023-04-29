# Use open functions to read the content of file!
my_file = open("C:\\Users\\DIGANTA\\WORKSPACE\\PYTHON\\diganta.txt",'r')
# data=my_file.read()
data=my_file.read(5) # reads first 5 character of the file
print(data)
my_file.close()
# print(my_file.read())