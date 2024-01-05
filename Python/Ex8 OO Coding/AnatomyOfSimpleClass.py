'''
Python script for: Anatomy of a simple class
Date: 05JAN2024
By: Shahanawaz Shaikh
'''

# Defining a class 'Person'
class Person:
    # Using the Constructor method to initialize the attributes, called whenever an instance of class is created
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Method to display information about the person
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Create instances (objects) of the 'Person' class
person1 = Person("Shan", 33)
person2 = Person("Saba", 30)
# Access attributes and call methods of the objects
print("Information about person1:")
person1.display_info()
print("\nInformation about person2:")
person2.display_info()
