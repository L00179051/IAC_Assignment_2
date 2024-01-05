'''
Python script for: Loops
Date: 05JAN2024
By: Shahanawaz Shaikh
'''

# Printing all values in variable
numbers = [1,2,3,4,5]
for i in numbers:
    print(i)

# Printing odd values in the variable
for i in numbers:
    if i %2 != 0:
        print(i)

# Sum the values in the array
total = 0
for i in numbers:
    total = total + i
print(total)

# Calculating the number of occurences a letter has appeared in a String.
Occurences = 0
for i in "Shahanawaz Shaikh":
    if i == 'a':
        Occurences = Occurences + 1
print(f"Number of Occurences for the Character 'a' is {Occurences}")

# Extracting values from variable of type Dictionary
scan = {"SMTP_PORT":"25","HTTPS_PORT":"443"}
print(type(scan))
for port, num in scan.items():
    print(f"The port is {port} and the port number is {num}")