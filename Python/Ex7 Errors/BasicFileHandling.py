'''
Python script for: Basic File Handling
Date: 05JAN2024
By: Shahanawaz Shaikh
'''

# Writing to a file
output_file_path = 'output.txt'

try:
    with open(output_file_path, 'w') as output_file:
        output_file.write("This is a sample text from Excercise 7 - Basic File Handling.\n")
        output_file.write("Using Python, writing to a file.")
    print(f"Content written to '{output_file_path}'.")
except Exception as e:
    print(f"An error occurred: {e}")
