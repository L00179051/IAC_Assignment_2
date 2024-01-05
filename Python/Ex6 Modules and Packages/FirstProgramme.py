'''
Python script for: First Programme
Date: 05JAN2024
By: Shahanawaz Shaikh
'''

# Importing platform library so that function to detect the current OS can be used.
import platform

def detect_os() ->str:
    return platform.system()

os = detect_os().lower()

if os == "windows": print(f"You are currently using Windows Operating System, the best of all OS")
else: print(f"Not a Windows computer. Microsoft recomends to use a Windows Operating System.")
