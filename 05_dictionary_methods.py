myDict={
    "fast":"In a Quick Manner",
    "jerry":"A Coder",
    "marks":[1,2,5],
    "anotherdict":{'jerry':'Player'},
    1: 2
}

# Dictionary methods
print(list(myDict.keys())) # Print the keys of the dictionary
print(myDict.values()) # Print the values of dictionary 
print(myDict.items()) # Print the (key,values) for all contents of dictionary 
print(myDict)
updateDict={
    'Lovish':'Friend',
    'Shubham':'Friend'
}
# myDict.update(updateDict) # Updates the dictionary by adding key values pairs from updateDict
print(myDict)

print(myDict.get("jerry")) # Prints value associated with key "jerry"
# The difference between .get and [] syntax in dictionary
print(myDict.get("jerry2")) # Returns none as jerry2 is not present in the diictionary 
print(myDict["jerry2"]) # it throws an error as jerry2 is not present in the dictionary
