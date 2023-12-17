# Open the file "user/shopping.txt" in read mode and print its content
file = open("user/shopping.txt", "r")
content = file.read()
print(content)
file.close()

# Open the file again in read mode, read lines, and print them
file = open("user/shopping.txt", "r")
content = file.readlines()
print(content)
file.close()

# Open the file in write mode, write some items, and close the file
file = open("user/shopping.txt", "w")
file.write("Microsoft\n")
file.write("Dell\n")
file.write("HP\n")
file.close()

# Open the file in append mode, add more items, and close the file
file = open("user/shopping.txt", "a")
file.write("Motorola\n")
file.write("Sony\n")
file.write("PlayStation\n")
file.close()

# Using 'with' statement to open the file in append mode and add more items
with open("user/shopping.txt", "a") as file:
    file.write("Lagos\n")
    file.write("Abuja\n")
    file.write("Canada\n")

# Open the file in read mode using 'with' statement, read lines, and print them
with open("user/shopping.txt", "r") as file:
    content = file.readlines()
    print(content)
