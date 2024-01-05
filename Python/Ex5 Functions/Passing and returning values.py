'''
Python script for: Passing and returning values
Date: 05JAN2024
By: Shahanawaz Shaikh
'''

def calculateCircumference(radius):
    """
    This is a function that takes input as radius and calculates the circumference
    """
    c = radius * 3.142 * 2
    print(f"The circumference for the radius - {radius} is {c} ")
    return c
# Calling Function
c = calculateCircumference(24)
print(f"The value returned can also be printed here {c}")


def add(a, b):
    """
    This is a function that sums two numbers passed
    """
    sum = a + b
    return sum
total = add(2,3)
print("Sum:", total)
