'''
Python script for: If Elif and Else.py
Date: 02DEC2023
By: Shahanawaz Shaikh
'''

# Age Input and check if minor, adult or senior citizen
age = int(input("Enter your age: "))

if age < 18:
    print("You are minor.")
elif 18 <= age < 65:
    print("You are an adult.")
else:
    print("You are senior citizen.")

