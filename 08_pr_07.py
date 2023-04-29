def remove_and_strip(string,word):
    newStr=string.replace(word,"")
    return newStr.strip()


this="   Jerry is a good   "
n=remove_and_strip(this,"Jerry")
print(n)

# print(this)
# print(this.strip())