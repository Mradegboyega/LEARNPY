#   A list is an ordered collection of data that can be changed.
#   - A list is defined using square brackets.
#   - A list can contain zero or more elements.
#   - A list can contain elements of different types. including other lists.
#   - A list can contain duplicate elements.

# Initial list of names
names = ["Michelle", "Toyin", "Tiaraoluwa", "Gboyega", "Adunni", "Kay"]

# Remove "Adunni" from the list
names.remove("Adunni")

# Remove the element at index 2 (which is "Tiaraoluwa") from the list
names.pop(2)

# Append "samson" to the end of the list
names.append("Samson")

# Print the modified list
print(names)

# Iterate through the list and print each name
for name in names:
    print(name)
