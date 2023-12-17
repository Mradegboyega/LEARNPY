from abc import ABC, abstractmethod

# Define an abstract class 'Product' with abstract methods
class Product(ABC):

    @abstractmethod
    def get_details(self):
        pass

    @abstractmethod
    def get_price(self):
        pass

# Define a concrete class 'Book' that inherits from 'Product'
class Book(Product):

    def __init__(self, name, price, author) -> None:
        self.name = name
        self.price = price
        self.author = author

    def get_details(self):
        return f"{self.name} by {self.author}"

    def get_price(self):
        return self.price

    def get_name(self):  # Corrected method name to match the abstract class
        return self.name

# Create an instance of the 'Book' class
book1 = Book("Harry", 20, "J.k Rowling")

# Print details, price, and name of the book
print(book1.get_details())
print(book1.get_price())
print(book1.get_name())
