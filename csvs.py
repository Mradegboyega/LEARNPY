# Open a CSV file and read its content
with open("user/users.csv", "r") as file:
    content = file.read()
    print(content)

# Open a CSV file and print its contents line by line
with open("user/users.csv", "r") as file:
    for line in file:
        print(line)

# Open a CSV file and print its content using the csv module
import csv

with open("user/users.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
