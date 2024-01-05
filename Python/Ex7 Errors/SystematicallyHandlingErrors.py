'''
Python script for: Systematically Handling Errors
Date: 05JAN2024
By: Shahanawaz Shaikh
'''

# Example of using try-except for handling an exception

# Get input
try:
    # Attempt to convert user input to an integer
    user_input = input("Enter an integer: ")
    user_input_int = int(user_input) #If conversion fails, it moves to except
    # Print the result
    print("You entered:", user_input_int)
    # return True
# Handle the ValueError exception if conversion fails
except ValueError:
    print("Invalid input. Please enter a valid integer.")
    #return False