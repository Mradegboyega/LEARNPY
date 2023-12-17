# Condition that checks for voter's eligibility

age = int(input("Enter your age: "))

if age >= 18:
    print("You're eligible to vote")
else:
    print("You can't vote until you are 18.")

# Condition that checks for marital status before accessing benefit

is_married = input("Are you married? (True or False): ").lower() == 'true'

if is_married:
    print("Welcome to our facility")
else:
    print("You're not eligible to use our service")

# Condition that checks the password to grant access

password = input("Enter your password: ")

if password == "12345":
    print("Access granted")
else:
    print("Incorrect password! Try again.")


