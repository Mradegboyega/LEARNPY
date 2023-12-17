def add(x, y):
    return x + y

def subtract(x, y):  # Fix the function name here
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        # raise an exception
        raise Exception("Not divisible")
    return x / y
