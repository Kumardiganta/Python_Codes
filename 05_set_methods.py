# Creating an empty set
b=set()
print(type(b))

# Adding values to an empty set
b.add(4)
b.add(4)
b.add(5)
b.add(5) # Adding a value repeatedly doesnot changes a set
b.add((4,5,6))
# b.add({4,5}) # Cannot add list or dictionary to sets
print(b)

## Accesing elements
print(len(b)) # Prints the length of this set

b.remove(5) # Removes 5 from the set b
# b.remove(15) # thorws an error while trying to remove 15 (which is not present in the st)
print(b)

print(b.pop())