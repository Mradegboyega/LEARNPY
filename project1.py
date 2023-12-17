# Define the correct username and password
correct_username = 'mradegboyega'
correct_password = '12345'

# Prompt the user for input
user_input_username = input('Enter your username: ')
user_input_password = input('Enter your password: ')

# Check if the entered username and password match the correct values
if user_input_username == correct_username and user_input_password == correct_password:
    print("Authentication successful. Access Granted!")
else:
    # If the entered credentials are incorrect, print an error message five times
    print("Incorrect credentials. Try again!")
    print("Incorrect credentials. Try again!")
    print("Incorrect credentials. Try again!")
    print("Incorrect credentials. Try again!")
    print("Incorrect credentials. Try again!")
