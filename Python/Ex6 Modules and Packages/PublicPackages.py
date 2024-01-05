'''
Python script for: Public Packages - Package Installer for Python (PIP)
Date: 05JAN2024
By: Shahanawaz Shaikh
'''

# To install requests library which is commonly used for making HTTP requests. 
# Open a terminal or command prompt and run the following command:
# pip install requests

# Run below to upgrade PIP
# pip install --upgrade pip
# Validate: pip -h


import requests
# Make a GET request to a sample URL
response = requests.get("https://atu.ie")

# Print the status code and content of the response
print("Status Code:", response.status_code)
# print("Response Content:\n", response.text)
