'''
Python script for: Time
Date: 05JAN2024
By: Shahanawaz Shaikh
'''

#Importing standard library
from datetime import datetime as dt
current_time = dt.now()
print(f"Current time: {current_time}")
print(f"Formatted time: {current_time.strftime("%Y-%m-%d")}")

print(dt.timestamp(current_time)) # Did not understand the timestamp function.