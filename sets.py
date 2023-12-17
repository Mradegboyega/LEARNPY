# A Set is an unordered collection of unique elements.
# A set can be created by placing elements inside curly braces.
# A set can be created by using the set() constructor.
# A set can contain values of different types.
# A set cannot contain duplicate values.
# A set is mutable, which means that its values can be changed.

# Create a set of strings
names = {"Michelle", "Toyin", "Tiaraoluwa", "gboyega", "Adunni", "Kay"}

# Create a set of integers
numbers = {1, 2, 3, 4, 5}

# Create a set of strings and integers
mixed_values = {"Bella", 1, "Charlie", 2, "Luna", 3}

# Create an empty set using set()
empty_set = set()

# Add "Tracy" to the 'names' set
names.add("Tracy")

# Remove "Kay" from the 'names' set
names.remove("Kay")

# Iterate through the 'names' set and print each name
for name in names:
    print(name)
