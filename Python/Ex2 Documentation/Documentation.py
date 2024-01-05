'''
Python script for: Documentation
Date: 21OCT2023
By: Shahanawaz Shaikh
Version: 1.1
'''

# File Headers
# If running in Linux, can start with a shebang
#!/usr/bin/env python

# Commenting code
count = 0
while count < 3:
    # s1 = input("Enter email address: ")
    s1 = "a@a.com"
    if (s1.__contains__('@') and s1.__contains__('.')): #To check if email address specified is valid.
        print("Email address is valid.")
        break
    print("Please provide a valid email address")
    count = count + 1
    print("Attempts remaining:" + str(3 - count)) # Counts the remaining attempts allowed

#Documentation
def hello_world(name):
    """Example of docstring"""
    print(f"Good Morning {name}")
hello_world("Shah") #Calling defined function
help(hello_world) #Docstring specified above under def is returned

#Writing Doc example:
'''
    Purpose: Values in the script are static and are not expected to be changed unless specified by the Vendor/Supplier.
'''

