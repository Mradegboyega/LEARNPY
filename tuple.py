# A tuple is a collection of values separated by commas.
# A tuple is immutable, which means that its values cannot be changed.
# - A tuple can be created by placing values inside parentheses.
# - A tuple can be created by placing values separated by commas.
# - A tuple can be created by using the tuple() constructor.
# - A tuple can contain values of different types.
# - A tuple can contain duplicate values.
# - A tuple can contain another tuple.

# Create a tuple of strings
names = ("Michelle", "Toyin", "Tiaraoluwa", "gboyega", "Adunni", "Kay")

# Create a tuple of integers
numbers = (1, 2, 3, 4, 5)

# Create a tuple of strings and integers
mixed = ("Bella", 1, "Charlie", 2, "Luna", 3)

# Create a tuple of lists
nested = (["Bella", "Charlie"], ["Luna", "Lucy"], ["Max", "Bailey"])

# Create an empty tuple
empty = ()

# Print the first two elements of the 'names' tuple
print(names[:2])

# Print elements starting from index 2 to the end of the 'names' tuple
print(names[2:])

# Iterate through the 'names' tuple and print each name
for name in names:
    print(name)
