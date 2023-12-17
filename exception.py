# When building robust programs, it's essential to handle errors and exceptions gracefully.
# The 'try' block is used to execute code that may potentially raise an exception.

try:
    result = 1 / 0  # Attempting a division that may result in a ZeroDivisionError.
except ZeroDivisionError:
    # If a 'ZeroDivisionError' occurs, the following block will handle it.
    print("Error: Division by zero.")

# The 'except' clause is where specific exceptions are caught and handled.

# In this example, we catch the more general 'Exception' class to handle unexpected errors.
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    # The 'else' block is executed if no exception is raised in the 'try' block.
    print("No exception occurred. The result is:", result)


# The 'try' block is used to execute code that may potentially raise an exception.
try:
    print(1 / 0)  # Attempting a division that may result in a ZeroDivisionError.
except ZeroDivisionError:
    # The 'except' block for ZeroDivisionError is executed if a division by zero occurs.
    print("Error: Division by zero")
except ValueError:
    # This 'except' block will not be executed because the division by zero will raise a ZeroDivisionError first.
    print("Error: Invalid value")


# Example 1: Handling division by zero using try, except, and else

try:
    result = 3 / 1  # Performing a division operation
except ZeroDivisionError:
    # The 'except' block for ZeroDivisionError is not executed since the division is successful.
    print("Error: Division by zero")
else:
    # The 'else' block is executed because no exception occurred in the 'try' block.
    print("Division successful")

# Example 2: Handling division by zero using try, except, else, and finally

try:
    result = 1 / 0  # Attempting to divide by zero
except ZeroDivisionError:
    # The 'except' block for ZeroDivisionError is executed due to division by zero.
    print("Error: Division by zero")
finally:
    # The 'finally' block is always executed, providing a place for cleanup or finalization code.
    print("Finally block executed, regardless of exceptions.")


# Define a function that performs division and raises a ZeroDivisionError if the denominator is zero
def divide(a, b):
    if b == 0:
        # Raise a ZeroDivisionError with a custom error message
        raise ZeroDivisionError("Error: Division by zero")
    return a / b

# Call the function with arguments (1, 0), which will raise a ZeroDivisionError
try:
    result = divide(1, 0)
except ZeroDivisionError as e:
    # Handle the raised ZeroDivisionError and print the error message
    print(f"Caught an exception: {e}")

# Assertions are used to check if conditions are true.
# If the condition is false, an AssertionError is raised.
# Assertions are primarily used to check for programmer errors.

# Raise an AssertionError if a condition is False

def divide(a, b):
    # Raise an assertion error if b is 0
    assert b != 0, "Error: Division by zero"
    return a / b

# Call the function with arguments (2, 0), which will raise an AssertionError
try:
    result = divide(2, 0)
except AssertionError as e:
    # Handle the raised AssertionError and print the error message
    print(f"Caught an assertion error: {e}")

