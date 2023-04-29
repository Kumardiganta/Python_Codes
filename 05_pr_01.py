myDict={
    "Pankha": "Fan",
    "Dabba": "Box",
    "Vastu": "Item"
}

print("Options are ",myDict.keys())
a=input("Enter the hindi word\n")
# print("The meanng of your word is: ",myDict[a])

# Below line will not throw an error if the key is not present in the dictionary
print("The meanng of your word is: ",myDict.get(a))