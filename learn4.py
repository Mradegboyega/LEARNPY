# Function to greet the user by taking their first and last names as input
def greet():
    # Prompt the user to enter their first name
    first_name = input("Enter your firstname: ")
    
    # Prompt the user to enter their last name
    last_name = input("Enter your lastname: ")
    
    # Return a welcome message with the user's full name
    return f"Welcome, {first_name} {last_name}."

# Call the greet function and print the result
print(greet())

